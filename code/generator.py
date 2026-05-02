import os
from groq import Groq
from typing import List, Dict


client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_response(issue: str, subject: str, context_chunks: List[Dict], company: str, request_type: str) -> str:
    # Use all retrieved chunks (up to TOP_K_RESULTS) with larger context window
    # Truncate each chunk to 2000 characters to fit more context within LLM limits
    context_parts = []
    for chunk in context_chunks:
        text = chunk['text']
        if len(text) > 2000:
            text = text[:2000] + "..."
        context_parts.append(text)
    
    context_text = "\n\n".join(context_parts)
    
    system_prompt = """You are a support agent. Answer only using information from the provided context.
Be concise (2-3 sentences max). If context doesn't fully address the issue, say so briefly and recommend escalation."""
    
    user_prompt = f"""Issue: {issue}
Company: {company}

Context (ground truth):
{context_text}

Provide a brief, helpful response:"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=200,
            temperature=0.1
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Unable to generate response. Please escalate to human agent."


def generate_invalid_response(issue: str) -> str:
    return "I'm sorry, but I cannot assist with this request as it is outside the scope of my capabilities. Please contact the appropriate support channel."