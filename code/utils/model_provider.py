"""
model_provider.py — Unified multi-provider LLM cascade with Azure OpenAI support.

Cascade order:
  1. Azure OpenAI (if configured)
  2. Gemini 2.0-flash (rotating keys)
  3. Groq llama-3.3-70b-versatile
"""

import json
import os
import time
import random
from google import genai
from google.genai import types as genai_types
import groq as _groq
from openai import OpenAI

from utils.api_rotator import rotator

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_AZURE_KEY = os.getenv("AZURE_OPENAI_API_KEY", "")
_AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "")
_AZURE_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "")

_GEMINI_MODEL = "gemini-2.0-flash"

_GROQ_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
]

# ---------------------------------------------------------------------------
# Provider Callers
# ---------------------------------------------------------------------------

def _call_azure(system_prompt: str, user_content: str, json_mode: bool) -> str:
    key = os.getenv("AZURE_OPENAI_API_KEY", "")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "")
    
    if not key or not endpoint or not deployment:
        raise RuntimeError("Azure OpenAI credentials missing")

    client = OpenAI(
        base_url=endpoint,
        api_key=key
    )
    
    kwargs = {}
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}

    # Parallel-safe retry loop for rate limits
    for attempt in range(5):
        try:
            resp = client.chat.completions.create(
                model=deployment,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user",   "content": user_content},
                ],
                temperature=1.0,
                **kwargs
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            err_msg = str(e)
            # If Azure blocks for safety or invalid request, we shouldn't retry with Azure
            if "400" in err_msg or "content_filter" in err_msg.lower():
                print(f"  [Azure] Request blocked/invalid (possibly safety filter). Shifting provider...")
                raise RuntimeError(f"AZURE_SAFETY_BLOCK: {err_msg}")
            
            if ("429" in err_msg or "rate limit" in err_msg.lower()) and attempt < 4:
                # Exponential backoff with jitter
                wait_time = (2 ** attempt) + random.random()
                print(f"  [Azure] Rate limited. Retrying in {wait_time:.2f}s (Attempt {attempt+1}/5)...")
                time.sleep(wait_time)
                continue
            raise e
    return ""


def _call_gemini(system_prompt: str, user_content: str, json_mode: bool) -> str:
    client = rotator.get_client()
    if not client:
        raise RuntimeError("No Gemini client available")

    mime = "application/json" if json_mode else "text/plain"
    response = client.models.generate_content(
        model=_GEMINI_MODEL,
        contents=[user_content],
        config=genai_types.GenerateContentConfig(
            system_instruction=system_prompt,
            response_mime_type=mime,
        ),
    )
    return response.text.strip()


def _call_groq(model: str, system_prompt: str, user_content: str, json_mode: bool) -> str:
    api_key = os.getenv("GROQ_API_KEY", "")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set")

    client = _groq.Groq(api_key=api_key)
    kwargs = {}
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}

    for attempt in range(3):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user",   "content": user_content},
                ],
                temperature=0.2,
                **kwargs,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            if "429" in str(e) and attempt < 2:
                time.sleep(2 ** attempt + random.random())
                continue
            raise e
    return ""

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def call_llm(system_prompt: str, user_content: str, json_mode: bool = False) -> str:
    errors = []

    # 1. Azure OpenAI (Top priority if configured)
    if os.getenv("AZURE_OPENAI_API_KEY"):
        try:
            result = _call_azure(system_prompt, user_content, json_mode)
            print("  [Provider] Azure OpenAI used")
            return result
        except Exception as e:
            print(f"  [DEBUG] Azure failed: {e}")
            errors.append(f"Azure: {str(e)[:80]}")

    # 2. Gemini (Rotated Keys)
    for attempt in range(rotator.key_count() + 1):
        try:
            return _call_gemini(system_prompt, user_content, json_mode)
        except Exception as e:
            err = str(e)
            if "RESOURCE_EXHAUSTED" in err or "429" in err:
                rotator.rotate()
                errors.append(f"Gemini[{attempt}]: quota")
                continue
            errors.append(f"Gemini: {err[:80]}")
            break

    # 3. Groq Fallback
    for model in _GROQ_MODELS:
        try:
            result = _call_groq(model, system_prompt, user_content, json_mode)
            print(f"  [Provider] Groq/{model} used as fallback")
            return result
        except Exception as e:
            errors.append(f"Groq/{model}: {str(e)[:80]}")

    raise RuntimeError(f"All providers failed: {errors}")