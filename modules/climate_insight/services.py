from core.llm_engine.factory import get_llm_provider

def generate_risk_report(location: str, risk_type: str) -> str:
    """
    Service to generate a climate risk report using the configured LLM.
    """
    provider = get_llm_provider()
    
    prompt = (
        f"Generate a professional climate risk assessment for {location}. "
        f"Focus on {risk_type}. Provide actionable insights and recommendations."
    )
    
    report = provider.generate_text(prompt)
    return report
