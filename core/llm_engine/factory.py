import importlib
from django.conf import settings
from .base import BaseLLMProvider

def get_llm_provider() -> BaseLLMProvider:
    """
    Factory function to initialize the LLM provider based on settings.
    """
    provider_name = getattr(settings, 'LLM_PROVIDER', 'gemini').lower()
    
    providers = {
        'gemini': 'core.llm_engine.providers.gemini.GeminiProvider',
        'openai': 'core.llm_engine.providers.openai.OpenAIProvider',
        'deepseek': 'core.llm_engine.providers.deepseek.DeepSeekProvider',
    }
    
    if provider_name not in providers:
        raise ValueError(f"Unsupported LLM provider: {provider_name}")
    
    module_path, class_name = providers[provider_name].rsplit('.', 1)
    module = importlib.import_module(module_path)
    provider_class = getattr(module, class_name)
    
    return provider_class()
