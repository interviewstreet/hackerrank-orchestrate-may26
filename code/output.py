"""
Output: Write results to CSV strictly as per challenge requirements.
"""

import csv
from pathlib import Path
from typing import List, Dict, Any


def write_output_csv(
    results: List[Dict[str, Any]],
    output_path: str,
    input_columns: List[str] = None
) -> None:
    """
    Write results to output CSV with exactly the required columns.
    """
    if not results:
        print(f"[Output] No results to write")
        return
    
    # Headers exactly as requested by the challenge and sample
    all_columns = ['Issue', 'Subject', 'Company', 'status', 'product_area', 'response', 'justification', 'request_type']
    
    print(f"[Output] Writing {len(results)} rows to {output_path}")
    
    try:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=all_columns)
            writer.writeheader()
            
            for result in results:
                row = {
                    'Issue': result.get('input_issue', ''),
                    'Subject': result.get('input_subject', ''),
                    'Company': result.get('input_company', ''),
                    'status': result.get('status', ''),
                    'product_area': result.get('product_area', ''),
                    'response': result.get('response', ''),
                    'justification': result.get('justification', ''),
                    'request_type': result.get('request_type', '')
                }
                writer.writerow(row)
        
        print(f"[Output] Successfully wrote {len(results)} rows")
    
    except Exception as e:
        print(f"[Output] Error writing CSV: {e}")
        raise


def validate_result(result: Dict[str, Any]) -> bool:
    """Check if a result has all required fields."""
    required_fields = [
        'status', 'product_area', 'response', 'justification', 'request_type'
    ]
    return all(field in result for field in required_fields)
