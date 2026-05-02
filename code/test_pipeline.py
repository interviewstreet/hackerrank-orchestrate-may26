"""
Lightweight unit tests for deterministic pipeline stages.
No LLM calls, no API keys needed.

Run: python code/test_pipeline.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from gatekeeper import GatekeeperResult, make_error_row, validate


def test_gatekeeper_happy_path():
    r = validate({"issue": "My screen share is broken", "subject": "Screen issue", "company": "HackerRank"}, 1)
    assert r.ok
    assert r.company == "HackerRank"
    assert r.issue == "My screen share is broken"
    assert r.subject == "Screen issue"
    print("PASS test_gatekeeper_happy_path")


def test_gatekeeper_company_normalise():
    for raw, expected in [
        ("hackerrank", "HackerRank"),
        ("VISA", "Visa"),
        ("claude", "Claude"),
        ("none", "None"),
        ("Google", "None"),
        ("", "None"),
    ]:
        r = validate({"issue": "test", "subject": "", "company": raw}, 1)
        assert r.company == expected, f"Expected {expected!r} got {r.company!r} for {raw!r}"
    print("PASS test_gatekeeper_company_normalise")


def test_gatekeeper_truncation():
    long_issue = "A" * 3000
    long_subject = "B" * 500
    r = validate({"issue": long_issue, "subject": long_subject, "company": "Visa"}, 1)
    assert len(r.issue) + len(r.subject) <= 2000
    assert len(r.issue) >= 200
    print("PASS test_gatekeeper_truncation")


def test_gatekeeper_short_issue_preserved():
    r = validate({"issue": "short", "subject": "", "company": "Claude"}, 1)
    assert r.issue == "short"
    print("PASS test_gatekeeper_short_issue_preserved")


def test_gatekeeper_error_row():
    row = make_error_row("req_001_1_123", "test error")
    assert row["status"] == "escalated"
    assert row["response"] == "Escalate to a human"
    assert "req_001_1_123" in row["justification"]
    print("PASS test_gatekeeper_error_row")


def test_gatekeeper_request_id_format():
    r = validate({"issue": "test", "subject": "", "company": "HackerRank"}, 42, epoch_ms=1000)
    assert r.request_id == "req_042_1_1000"
    print("PASS test_gatekeeper_request_id_format")


def test_gatekeeper_missing_fields():
    r = validate({}, 1)
    assert r.ok
    assert r.issue == ""
    assert r.company == "None"
    print("PASS test_gatekeeper_missing_fields")


def test_constants():
    from anchor import GROUNDING_THRESHOLD
    from verifier import CONFIDENCE_THRESHOLD
    assert GROUNDING_THRESHOLD == 0.35
    assert CONFIDENCE_THRESHOLD == 0.50
    print("PASS test_constants")


def test_output_columns():
    import agent
    assert agent.OUTPUT_COLUMNS == ["status", "product_area", "response", "justification", "request_type"]
    assert agent.ESCALATION_RESPONSE == "Escalate to a human"
    print("PASS test_output_columns")


if __name__ == "__main__":
    tests = [
        test_gatekeeper_happy_path,
        test_gatekeeper_company_normalise,
        test_gatekeeper_truncation,
        test_gatekeeper_short_issue_preserved,
        test_gatekeeper_error_row,
        test_gatekeeper_request_id_format,
        test_gatekeeper_missing_fields,
        test_constants,
        test_output_columns,
    ]
    failed = 0
    for t in tests:
        try:
            t()
        except AssertionError as e:
            print(f"FAIL {t.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"ERROR {t.__name__}: {e}")
            failed += 1
    print(f"\n{len(tests) - failed}/{len(tests)} tests passed")
    sys.exit(1 if failed else 0)
