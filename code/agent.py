import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

SYSTEM_PROMPT = """You are a support triage agent. Your goal is to process support tickets based ONLY on the provided context.

RULES:
1. Use ONLY the provided context chunks. If the answer isn't there, state that you cannot answer and escalate if it seems important.
2. Do NOT hallucinate policies or external links.
3. Escalate (status: "escalated") if the ticket involves sensitive issues (billing, fraud, security) or if the provided context is insufficient.
4. If you can answer, set status to "replied" and provide a helpful response.
5. Output MUST be valid JSON. No preamble, no markdown formatting.

JSON Schema:
{
  "status": "replied" | "escalated",
  "product_area": "string",
  "response": "string",
  "justification": "string",
  "request_type": "product_issue" | "feature_request" | "bug" | "invalid"
}"""

def process_ticket(ticket: dict, context_chunks: list[dict]) -> dict:
    issue = ticket.get('issue', '')
    subject = ticket.get('subject', '')
    company = ticket.get('company', 'Unknown')
    
    context_text = "\n\n".join([f"Context [{i+1}]:\n{c['text']}" for i, c in enumerate(context_chunks)])
    
    user_message = f"""{SYSTEM_PROMPT}

Ticket Info:
Subject: {subject}
Company: {company}
Issue: {issue}

Context:
{context_text}"""

    def call_llm(extra_instruction=""):
        prompt = f"{user_message}\n{extra_instruction}"
        
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.1,
                max_output_tokens=1000,
            )
        )
        
        content = response.text
        try:
            # Clean possible markdown wrap
            content = content.strip()
            if content.startswith("```json"):
                content = content[7:-3].strip()
            elif content.startswith("```"):
                content = content[3:-3].strip()
            return json.loads(content)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON: {content}") from e

    try:
        return call_llm()
    except Exception:
        # Retry once with stricter instruction
        try:
            return call_llm(extra_instruction="IMPORTANT: Return ONLY raw JSON. No markdown, no conversational text.")
        except Exception:
            return {
                "status": "escalated",
                "product_area": "Unknown",
                "response": "I encountered an error processing your request. Escalating to a human agent.",
                "justification": "JSON parsing error after retry.",
                "request_type": "product_issue"
            }
