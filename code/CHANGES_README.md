# Changes Made

## Strict Grounding System Implementation

### Key Changes

1. **Hard Grounding Enforcement** (pipeline.py)
   - `grounded = retrieval_score >= RETRIEVAL_THRESHOLD and chunks_exist`
   - If not grounded → escalate

2. **Forbidden Pattern Blocking** (pipeline.py + llm_agent.py)
   - Blocks responses containing: "try", "ensure", "check your", "make sure", etc.
   - If detected → escalate

3. **Context-Only Generation** (llm_agent.py)
   - LLM must ONLY use retrieved context
   - No inference, expansion, or missing step fabrication

4. **Post-Generation Guardrails** (pipeline.py)
   - Grounding check: word overlap with context
   - Length constraint: max 120 words
   - Vague response detection

5. **Response Templates**
   - `SAFE_ESCALATION_RESPONSE = "This issue requires further investigation and has been escalated to support."`
   - `SAFE_REFUSAL_RESPONSE = "I cannot assist with that request."`

6. **Status Alignment**
   - If response is escalation message → status = "escalated"
   - If response is refusal message → status = "replied"

## Files Modified

- `pipeline.py` - Decision engine with guardrails
- `agents/llm_agent.py` - Strict generation prompt
- `agents/pre_safe.py` - Safety keywords
- `agents/grounding.py` - Request type fix
- `config.py` - Keywords and thresholds

## Dependencies

```bash
pip install -r requirements.txt
```

## Running

```bash
cd code
source venv/bin/activate
python main.py
```

Output: `../support_tickets/output.csv`