## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
cd code/
python main.py \
  --tickets ../support_tickets/support_tickets.csv \
  --data ../data/ \
  --output ../support_tickets/output.csv \
  --log ../run_log.txt
```

## Validation

```bash
cd code/
python main.py \
  --tickets ../support_tickets/sample_support_tickets.csv \
  --data ../data/ \
  --output ../support_tickets/sample_output.csv \
  --log ../run_log.txt
```

## Output columns

`status, product_area, response, justification, request_type`
