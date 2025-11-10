#!/usr/bin/env python3
"""
Test script to verify OpenRouter integration
"""

import requests

def test_openrouter_connection(api_key):
    """Test OpenRouter API connection"""
    if not api_key:
        print("❌ Please provide an API key")
        return False
    
    print("🧪 Testing OpenRouter connection...")
    
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": "http://localhost:8504",
            "X-Title": "Exercise Routine Generator Test",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "google/gemma-2-9b-it",
            "messages": [
                {"role": "user", "content": "Say hello in one sentence."}
            ]
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=30)
        
        if response.status_code == 401:
            print("❌ Invalid API key")
            return False
        elif response.status_code != 200:
            print(f"❌ Error: HTTP {response.status_code}")
            print(f"Response: {response.text}")
            return False
        
        result = response.json()
        
        if 'error' in result:
            print(f"❌ API Error: {result['error']}")
            return False
        
        if 'choices' in result and len(result['choices']) > 0:
            response_text = result['choices'][0]['message']['content']
            print(f"✅ OpenRouter working! Response: {response_text}")
            return True
        else:
            print("❌ No response received")
            return False
            
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

def main():
    print("🔍 OpenRouter Integration Test")
    print("=" * 40)
    
    # You can add a test API key here or input it
    test_api_key = input("Enter your OpenRouter API key (or press Enter to skip): ").strip()
    
    if test_api_key:
        if test_openrouter_connection(test_api_key):
            print("\n✅ OpenRouter integration is working!")
            print("🚀 You can now use OpenRouter models in the app")
        else:
            print("\n❌ OpenRouter test failed")
            print("💡 Check your API key and internet connection")
    else:
        print("⏭️ Skipped OpenRouter test")
        print("💡 To test OpenRouter, get an API key from https://openrouter.ai/keys")

if __name__ == "__main__":
    main()