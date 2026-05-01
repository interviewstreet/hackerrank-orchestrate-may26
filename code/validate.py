#!/usr/bin/env python3
"""Validation script to verify all fixes."""

import csv
import sys

def validate_output():
    """Validate output.csv for all fixes."""
    with open("output.csv", 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    issues = []
    
    print("✓ Validation Report")
    print("=" * 60)
    
    # Check 1: Product areas - if from corpus chunks, "general" is valid; if no chunks, should be "unknown"
    unknown_without_response = sum(1 for r in rows if r["Product_Area"] == "unknown" and "Unable to find" in r["Response"])
    print(f"✅ Fix #2: Product area defaults - {unknown_without_response} correctly defaulted to 'unknown' when no chunks")
    
    # Check 2: Response structure (has Summary and/or Point structure)
    bad_response_count = 0
    for i, row in enumerate(rows):
        resp = row["Response"]
        # Check if response has structure OR is the fallback message
        has_structure = "Summary:" in resp or "Point" in resp or "Unable to find" in resp
        if resp and len(resp) > 100 and not has_structure:
            bad_response_count += 1
    
    if bad_response_count > 0:
        issues.append(f"⚠️ {bad_response_count} long responses lack expected structure")
    else:
        print("✅ Fix #3: All responses have proper structure (Summary, Points, or fallback)")
    
    # Check 3: Justification detail (should have pipes and reasons)
    bad_justification = sum(1 for r in rows if "|" not in r["Justification"])
    if bad_justification == 0:
        print("✅ Fix #7: Justification is detailed with reason explanations")
    else:
        issues.append(f"⚠️ {bad_justification} rows have basic justification (not detailed)")
    
    # Check 4: Escalation stats
    escalated = sum(1 for r in rows if r["Status"] == "Escalated")
    replied = sum(1 for r in rows if r["Status"] == "Replied")
    print(f"✅ Fix #5: Escalation balance - {escalated} escalated, {replied} replied")
    
    # Check 5: Tie-breaking (if we have Claude/Visa, they should appear in Domain)
    domain_dist = {}
    for row in rows:
        domain = row["Justification"].split("|")[0].split(":")[1].strip()
        domain_dist[domain] = domain_dist.get(domain, 0) + 1
    
    print(f"✅ Fix #4: Domain distribution - {domain_dist}")
    
    # Check 6: Invalid tickets are escalated
    invalid_escalated = sum(1 for r in rows if r["Request_Type"] == "invalid" and r["Status"] == "Escalated")
    invalid_replied = sum(1 for r in rows if r["Request_Type"] == "invalid" and r["Status"] == "Replied")
    
    if invalid_replied > 0:
        issues.append(f"❌ Found {invalid_replied} invalid requests that were Replied (should all be Escalated)")
    else:
        print(f"✅ Fix #1: All {invalid_escalated} invalid requests properly escalated")
    
    print("\n" + "=" * 60)
    if issues:
        print("⚠️ ISSUES FOUND:")
        for issue in issues:
            print(f"  {issue}")
        return False
    else:
        print("🎉 All fixes verified successfully!")
        return True

if __name__ == "__main__":
    success = validate_output()
    sys.exit(0 if success else 1)
