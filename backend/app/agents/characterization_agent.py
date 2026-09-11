import logging
import json
from typing import Dict, Any
from app.agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)

class CharacterizationAgent(BaseAgent):
    """Characterizes the legal dispute"""
    
    def __init__(self):
        super().__init__("CharacterizationAgent")
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Private International Law attorney specializing in dispute characterization.
        Your task is to analyze case facts and characterize the legal dispute.
        Identify the dispute type, involved parties, jurisdictions, and PIL issues.
        Return JSON formatted response."""
    
    async def analyze(self, case_facts: Dict[str, Any]) -> Dict[str, Any]:
        """Characterize legal dispute"""
        prompt = f"""Analyze and characterize this legal dispute:
        
        Facts: {json.dumps(case_facts, indent=2)}
        
        Provide:
        1. Dispute Type (contract, tort, property, family, etc.)
        2. Involved Parties and their jurisdictions
        3. Key PIL Issues
        4. Potential Jurisdictions Involved
        5. Preliminary Assessment
        
        Return as JSON."""
        
        response = await self.call_llm(prompt)
        
        try:
            result = json.loads(response)
        except:
            result = {"raw_analysis": response}
        
        logger.info(f"Characterization analysis complete for dispute type: {result.get('dispute_type', 'unknown')}")
        return result
