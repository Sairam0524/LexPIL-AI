import logging
import json
from typing import Dict, Any
from app.agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)

class JurisdictionAgent(BaseAgent):
    """Determines jurisdiction for the dispute"""
    
    def __init__(self):
        super().__init__("JurisdictionAgent")
    
    def _get_system_prompt(self) -> str:
        return """You are an expert in Private International Law jurisdiction rules.
        Analyze disputes to determine territorial jurisdiction, personal jurisdiction,
        subject matter jurisdiction, forum conveniens, and anti-suit injunctions.
        Consider rules from India, UK, Singapore, US, Australia.
        Return JSON formatted response."""
    
    async def analyze(self, case_facts: Dict[str, Any], dispute_type: str) -> Dict[str, Any]:
        """Analyze jurisdiction"""
        prompt = f"""Determine jurisdiction for this {dispute_type} dispute:
        
        Facts: {json.dumps(case_facts, indent=2)}
        
        Analyze:
        1. Territorial Jurisdiction
        2. Personal Jurisdiction over Defendants
        3. Subject Matter Jurisdiction
        4. Forum Conveniens Considerations
        5. Anti-Suit Injunction Risks
        6. Potential Jurisdictions
        7. Jurisdiction Rules Applicable
        
        Return as JSON with detailed analysis."""
        
        response = await self.call_llm(prompt)
        
        try:
            result = json.loads(response)
        except:
            result = {"raw_analysis": response}
        
        logger.info(f"Jurisdiction analysis complete")
        return result
