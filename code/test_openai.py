"""
test_openai.py
Quick test to verify OpenAI API is working correctly.
Run: python test_openai.py
"""

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from config import OPENAI_API_KEY, LLM_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS
from openai import OpenAI

def test_basic_api():
    """Test basic OpenAI API connectivity."""
    print("=" * 60)
    print("Testing OpenAI API Setup")
    print("=" * 60)
    
    # Check API key
    if not OPENAI_API_KEY or OPENAI_API_KEY.startswith("sk-proj-"):
        print("✅ API Key loaded from config")
        print(f"   Key (masked): {OPENAI_API_KEY[:20]}...{OPENAI_API_KEY[-10:]}")
    else:
        print("❌ API Key not found or invalid")
        return False
    
    print(f"✅ Model: {LLM_MODEL}")
    print(f"✅ Temperature: {LLM_TEMPERATURE}")
    print(f"✅ Max Tokens: {LLM_MAX_TOKENS}")
    print()
    
    # Initialize client
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        print("✅ OpenAI client initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize client: {e}")
        return False
    
    # Test API call
    print("\nTesting API call...")
    print("-" * 60)
    
    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            max_tokens=50,
            temperature=LLM_TEMPERATURE,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say 'OpenAI API is working!' in one sentence."}
            ],
        )
        
        result = response.choices[0].message.content
        print(f"✅ API Response: {result}")
        print("-" * 60)
        print()
        return True
        
    except Exception as e:
        print(f"❌ API call failed: {e}")
        print(f"   Error type: {type(e).__name__}")
        return False


def test_router_agent():
    """Test router agent with OpenAI."""
    print("=" * 60)
    print("Testing Router Agent")
    print("=" * 60)
    
    try:
        from agents.router import run as router_run
        
        test_queries = [
            ("I can't login to my Claude account", "claude"),
            ("How do I use HackerRank for recruiting?", "hackerrank"),
            ("My Visa card was declined", "visa"),
        ]
        
        print("\nTesting domain classification:")
        print("-" * 60)
        
        for query, expected_domain in test_queries:
            result = router_run(query, None)
            domain = result.get("domain")
            method = result.get("method")
            confidence = result.get("confidence")
            
            status = "✅" if domain == expected_domain else "⚠️"
            print(f"{status} Query: '{query}'")
            print(f"   Domain: {domain} (expected: {expected_domain})")
            print(f"   Method: {method}, Confidence: {confidence}")
        
        print("-" * 60)
        return True
        
    except Exception as e:
        print(f"❌ Router test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_llm_agent():
    """Test LLM agent with sample context."""
    print("=" * 60)
    print("Testing LLM Agent")
    print("=" * 60)
    
    try:
        # Import uses hyphen in filename
        import importlib
        llm_agent_module = importlib.import_module('agents.llm-agent')
        llm_run = llm_agent_module.run
        
        # Sample context
        sample_chunks = [
            {
                "text": "Claude is an AI assistant made by Anthropic. It can help with writing, analysis, coding, and more.",
                "score": 0.95,
                "metadata": {
                    "domain": "claude",
                    "product_area": "features",
                    "source_url": "https://example.com",
                    "title": "What is Claude?",
                    "heading": "Overview"
                }
            }
        ]
        
        test_query = "What is Claude?"
        
        print(f"\nQuery: {test_query}")
        print(f"Context chunks: {len(sample_chunks)}")
        print("-" * 60)
        
        result = llm_run(test_query, sample_chunks)
        
        print(f"Response: {result.get('response', 'N/A')[:100]}...")
        print(f"Request Type: {result.get('request_type', 'N/A')}")
        print(f"Escalate: {result.get('escalate', False)}")
        print("-" * 60)
        
        return True
        
    except Exception as e:
        print(f"❌ LLM agent test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    results = []
    
    # Test 1: Basic API
    results.append(("Basic API Connection", test_basic_api()))
    print()
    
    # Test 2: Router Agent
    results.append(("Router Agent", test_router_agent()))
    print()
    
    # Test 3: LLM Agent
    results.append(("LLM Agent", test_llm_agent()))
    print()
    
    # Summary
    print("=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    all_passed = all(result[1] for result in results)
    print()
    
    if all_passed:
        print("🎉 All tests passed! OpenAI API is working correctly.")
        return 0
    else:
        print("⚠️  Some tests failed. Check the output above.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
