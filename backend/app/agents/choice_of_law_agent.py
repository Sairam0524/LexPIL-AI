import logging
import json
from typing import Dict, Any, List
from app.agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)

class ChoiceOfLawAgent(BaseAgent):
    """Determines governing law"""
    
    def __init__(self):
        super().__init__("ChoiceOfLawAgent")
    
    def _get_system_prompt(self) -> str:
        return """You are an expert in Private International Law choice of law principles.
        Apply conflict of laws rules to determine the governing law for disputes.
        Consider express choice of law clauses, implied choice, proper law doctrine,
        and various jurisdictions' connecting factors.
        Return JSON formatted response."""
    
    async def analyze(self, case_facts: Dict[str, Any], dispute_type: str, 
                     potential_jurisdictions: List[str]) -> Dict[str, Any]:
        """Determine governing law"""
        prompt = f"""Determine the governing law for this {dispute_type} dispute:
        
        Facts: {json.dumps(case_facts, indent=2)}
        Potential Jurisdictions: {json.dumps(potential_jurisdictions, indent=2)}
        
        Analyze:
        1. Express Choice of Law
        2. Implied Choice of Law
        3. Proper Law Doctrine
        4. Connecting Factors
        5. Applicable Rules for {dispute_type} disputes
        6. Conflict Prevention Mechanisms
        7. Most Appropriate Governing Law
        
        Return as JSON with detailed analysis."""
        
        response = await self.call_llm(prompt)
        
        try:
            result = json.loads(response)
        except:
            result = {"raw_analysis": response}
        
        logger.info(f"Choice of law analysis complete")
        return result
