import logging
import json
from typing import Dict, Any, List
from app.agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)

class TreatyAgent(BaseAgent):
    """Analyzes applicable international treaties"""
    
    def __init__(self):
        super().__init__("TreatyAgent")
    
    def _get_system_prompt(self) -> str:
        return """You are an expert in international treaties affecting Private International Law.
        Identify and analyze relevant treaties like New York Convention, Hague Convention, CISG.
        Return JSON formatted response."""
    
    async def analyze(self, potential_jurisdictions: List[str]) -> Dict[str, Any]:
        """Analyze applicable treaties"""
        prompt = f"""Identify applicable international treaties:
        
        Potential Jurisdictions: {json.dumps(potential_jurisdictions, indent=2)}
        
        Identify:
        1. New York Convention on Recognition (1958)
        2. Hague Convention on Jurisdiction
        3. UNCITRAL Model Laws
        4. Bilateral Treaties
        5. Regional Treaties
        6. CISG Applicability
        7. Treaty Impact on Dispute
        
        Return as JSON with detailed analysis."""
        
        response = await self.call_llm(prompt)
        
        try:
            result = json.loads(response)
        except:
            result = {"raw_analysis": response}
        
        logger.info(f"Treaty analysis complete")
        return result
