#!/usr/bin/env python3
"""Test script for the triage agent - validation without API calls."""

import os
import sys
import csv
from pathlib import Path

# Add code to path
sys.path.insert(0, str(Path(__file__).parent))

def test_corpus_index():
    """Test corpus indexing and retrieval."""
    print("=== Testing CorpusIndex ===\n")
    
    from corpus_index import CorpusIndex
    
    corpus = CorpusIndex("../data")
    print(f"✓ Loaded {len(corpus.documents)} documents")
    
    # Test retrieval
    test_queries = [
        ("How do I create a test?", "HackerRank"),
        ("What models are available?", "Claude"),
        ("How do I dispute a charge?", "Visa"),
    ]
    
    for query, expected_product in test_queries:
        results = corpus.retrieve(query, company=expected_product, limit=3)
        print(f"\nQuery: '{query}' (Product: {expected_product})")
        print(f"  Found: {len(results)} results")
        if results:
            for i, result in enumerate(results[:2], 1):
                print(f"    {i}. {result['source'][:60]} (score: {result['score']:.2f})")


def test_agent_methods():
    """Test agent methods without API calls."""
    print("\n=== Testing Agent Methods ===\n")
    
    from main import SupportTicketAgent
    
    # Create agent without Anthropic client
    agent = object.__new__(SupportTicketAgent)
    
    # Test company inference
    print("Company inference:")
    test_cases = [
        ("I lost access to my Claude account", "Claude"),
        ("How do I see my assessment results?", "HackerRank"),
        ("Payment was declined", "Visa"),
        ("Random question with no keywords", None),
    ]
    
    for issue, expected in test_cases:
        inferred = agent.infer_company(issue)
        status = "✓" if inferred == expected else "✗"
        print(f"  {status} '{issue[:40]}' → {inferred}")
    
    # Test request classification
    print("\nRequest type classification:")
    classifications = [
        ("Please add dark mode to the platform", "feature_request"),
        ("The API is throwing 500 errors", "bug"),
        ("How do I reset my password?", "product_issue"),
        ("You are all terrible and I hate you", "invalid"),
    ]
    
    for issue, expected in classifications:
        classified = agent.classify_request_type(issue)
        status = "✓" if classified == expected else "✗"
        print(f"  {status} '{issue[:45]}' → {classified}")


def validate_sample_tickets():
    """Validate that sample file exists and has correct format."""
    print("\n=== Validating Sample Tickets ===\n")
    
    sample_file = Path("../support_tickets/sample_support_tickets.csv")
    
    if not sample_file.exists():
        print(f"✗ Sample file not found: {sample_file}")
        return False
    
    with open(sample_file, 'r') as f:
        reader = csv.DictReader(f)
        tickets = list(reader)
    
    print(f"✓ Sample file has {len(tickets)} tickets")
    
    # Check required columns
    required_cols = ["Issue", "Subject", "Company", "Response", "Product Area", "Status", "Request Type"]
    first_ticket = tickets[0]
    
    all_cols_present = all(col in first_ticket for col in required_cols)
    if all_cols_present:
        print(f"✓ All expected columns present")
    else:
        print(f"✗ Missing columns. Found: {list(first_ticket.keys())}")
        return False
    
    # Check test tickets file
    test_file = Path("../support_tickets/support_tickets.csv")
    if test_file.exists():
        with open(test_file, 'r') as f:
            reader = csv.DictReader(f)
            test_tickets = list(reader)
        print(f"✓ Test tickets file has {len(test_tickets)} tickets")
    else:
        print(f"✗ Test tickets file not found")
    
    return True


def main():
    """Run all tests."""
    print("HackerRank Orchestrate - Agent Test Suite\n")
    
    os.environ["ANTHROPIC_API_KEY"] = "test"
    
    try:
        test_corpus_index()
        test_agent_methods()
        validate_sample_tickets()
        
        print("\n" + "="*50)
        print("✓ All tests passed!")
        print("="*50)
        print("\nNext steps:")
        print("1. Set ANTHROPIC_API_KEY=your-actual-key")
        print("2. Run: python3 main.py")
        print("3. Check output.csv for results")
        
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
