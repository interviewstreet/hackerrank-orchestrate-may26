"""
test_openai_simple.py
Simple verification that OpenAI API key is working.
Run: python test_openai_simple.py
"""

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from config import OPENAI_API_KEY, LLM_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS

def test_api_key_and_client():
    """Test if API key is valid and client initializes."""
    print("=" * 70)
    print("OPENAI API VERIFICATION TEST")
    print("=" * 70)
    print()
    
    # Check API key exists
    print("1. Checking API Key...")
    print("-" * 70)
    
    if not OPENAI_API_KEY:
        print("❌ OPENAI_API_KEY is not set in .env or environment")
        print("   Set it: export OPENAI_API_KEY='sk-proj-your-key-here'")
        return False
    
    print(f"✅ API Key found: {OPENAI_API_KEY[:20]}...{OPENAI_API_KEY[-10:]}")
    print()
    
    # Check config
    print("2. Configuration Check...")
    print("-" * 70)
    print(f"   Model: {LLM_MODEL}")
    print(f"   Temperature: {LLM_TEMPERATURE}")
    print(f"   Max Tokens: {LLM_MAX_TOKENS}")
    print("✅ Config loaded successfully")
    print()
    
    # Initialize OpenAI client
    print("3. OpenAI Client Initialization...")
    print("-" * 70)
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)
        print("✅ OpenAI client initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize: {e}")
        return False
    
    print()
    
    # Test API call
    print("4. Testing API Call...")
    print("-" * 70)
    
    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            max_tokens=50,
            temperature=LLM_TEMPERATURE,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Respond briefly."
                },
                {
                    "role": "user",
                    "content": "Say 'OpenAI API is working!' in one sentence."
                }
            ],
        )
        
        result = response.choices[0].message.content.strip()
        print(f"✅ API Response: '{result}'")
        print()
        
        return True
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ API Call Failed")
        print(f"   Error: {error_msg}")
        print()
        
        # Provide helpful guidance
        if "401" in error_msg or "invalid_request_error" in error_msg:
            print("   ⚠️  Authentication Error - Your API key is invalid or expired")
            print("   👉 Get a new key from: https://platform.openai.com/account/api-keys")
            print("   👉 Update .env file: OPENAI_API_KEY=your_new_key")
        elif "rate_limit" in error_msg.lower():
            print("   ⚠️  Rate Limit Error - You've hit API rate limits")
            print("   👉 Wait a minute and try again")
        elif "model" in error_msg.lower():
            print(f"   ⚠️  Model Error - {LLM_MODEL} may not be available")
            print("   👉 Check available models at platform.openai.com")
        
        return False


def test_router_agent():
    """Test router agent without API calls."""
    print("5. Testing Router Agent (Keyword Matching)...")
    print("-" * 70)
    
    try:
        from agents.router import run as router_run
        
        test_cases = [
            ("I can't login to Claude", "claude"),
            ("HackerRank assessment not working", "hackerrank"),
            ("Visa card declined", "visa"),
        ]
        
        passed = 0
        for query, expected in test_cases:
            result = router_run(query, None)
            domain = result.get("domain")
            method = result.get("method")
            
            if domain == expected:
                print(f"✅ '{query}' → {domain} (via {method})")
                passed += 1
            else:
                print(f"⚠️  '{query}' → {domain} (expected {expected}, via {method})")
        
        print(f"   Result: {passed}/{len(test_cases)} tests passed")
        print()
        return passed == len(test_cases)
        
    except Exception as e:
        print(f"❌ Router test failed: {e}")
        print()
        return False


def main():
    """Run all tests."""
    
    # Test 1: API Key and Client
    api_ok = test_api_key_and_client()
    
    # Test 2: Router Agent
    router_ok = test_router_agent()
    
    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    if api_ok and router_ok:
        print("🎉 All tests passed!")
        print()
        print("✅ Your OpenAI API is configured and working correctly")
        print("✅ Router agent keyword matching is working")
        print()
        print("You can now run: python main.py --sample")
        return 0
    else:
        print("⚠️  Some tests failed:")
        if not api_ok:
            print("   - API connection failed (check API key)")
        if not router_ok:
            print("   - Router agent test failed")
        print()
        print("Next steps:")
        print("1. Update OPENAI_API_KEY in .env with a valid key")
        print("2. Run this test again: python test_openai_simple.py")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
