import csv
import json

# parse LLM response into a json object
def parse_response(response: str):
    return json.loads(response)

def write_output(file: str, data_obj):
    # define output fileds
    fields = ["status", "product_area", "response", "justification", "request_type"]
    with open(file, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(data_obj)
