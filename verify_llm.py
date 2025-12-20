import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.llm_engine.factory import get_llm_provider

def test_llm_factory():
    print("Testing LLM Factory...")
    try:
        provider = get_llm_provider()
        print(f"Successfully initialized provider: {provider.__class__.__name__}")
        
        test_prompt = "Hello, how are you?"
        response = provider.generate_text(test_prompt)
        print(f"Sample response: {response}")
        
        print("\nSUCCESS: LLM Factory is working correctly.")
    except Exception as e:
        print(f"\nFAILURE: {str(e)}")

if __name__ == "__main__":
    test_llm_factory()
