from abc import ABC, abstractmethod

class BaseLLMProvider(ABC):
    """
    Abstract Base Class for LLM Providers.
    """
    
    @abstractmethod
    def generate_text(self, prompt: str, **kwargs) -> str:
        """
        Generate text response for a given prompt.
        """
        pass
