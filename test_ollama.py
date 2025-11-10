#!/usr/bin/env python3
"""
Simple test script to verify Ollama is working with the available models
"""

import requests
import json
import sys

def test_ollama_connection():
    """Test if Ollama is running and responsive"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            print(f"✅ Ollama is running with {len(models)} models:")
            for model in models:
                name = model.get('name', 'Unknown')
                size_gb = model.get('size', 0) / (1024**3)
                print(f"   📦 {name} ({size_gb:.1f} GB)")
            return True, models
        else:
            print(f"❌ Ollama responded with status {response.status_code}")
            return False, []
    except Exception as e:
        print(f"❌ Cannot connect to Ollama: {e}")
        return False, []

def test_model(model_name):
    """Test if a specific model can generate responses"""
    print(f"\n🧪 Testing model: {model_name}")
    
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model_name,
        "prompt": "Say hello in one sentence.",
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data, timeout=30)
        result = response.json()
        
        if 'error' in result:
            print(f"❌ Model error: {result['error']}")
            return False
        else:
            response_text = result.get('response', 'No response')
            print(f"✅ Model working! Response: {response_text.strip()}")
            return True
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    print("🔍 Testing Ollama Setup for Exercise Routine Generator")
    print("=" * 60)
    
    # Test connection
    is_connected, models = test_ollama_connection()
    
    if not is_connected:
        print("\n❌ Please start Ollama first:")
        print("   1. Open a terminal")
        print("   2. Run: ollama serve")
        print("   3. Keep it running")
        return False
    
    # Test available models that should work with limited memory
    recommended_models = ["gemma2:2b", "gemma3:270m", "moondream:latest"]
    working_models = []
    
    for model_info in models:
        model_name = model_info.get('name', '')
        if any(rec in model_name for rec in recommended_models):
            if test_model(model_name):
                working_models.append(model_name)
    
    print(f"\n📊 Summary:")
    print(f"   Working models: {len(working_models)}")
    
    if working_models:
        print("✅ Setup is ready! You can use these models:")
        for model in working_models:
            print(f"   ✓ {model}")
        print(f"\n🚀 Start the app with: streamlit run app.py")
        print(f"   Or double-click: start_app.bat")
        return True
    else:
        print("❌ No working models found. Try downloading a smaller model:")
        print("   ollama pull gemma2:2b")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)