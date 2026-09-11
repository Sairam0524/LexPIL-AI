import logging
import json
from typing import Dict, Any
from app.agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)

class EnforcementAgent(BaseAgent):
    """Analyzes enforcement of judgments and awards"""
    
    def __init__(self):
        super().__init__("EnforcementAgent")
    
    def _get_system_prompt(self) -> str:
        return """You are an expert in enforcing foreign judgments and international arbitration awards.
        Analyze enforcement mechanisms, procedures, and obstacles under PIL.
        Consider public policy exceptions and local remedies doctrine.
        Return JSON formatted response."""
    
    async def analyze(self, case_facts: Dict[str, Any], recognition_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze enforcement issues"""
        prompt = f"""Analyze judgment and award enforcement issues:
        
        Case Facts: {json.dumps(case_facts, indent=2)}
        Recognition Analysis: {json.dumps(recognition_analysis, indent=2)}
        
        Analyze:
        1. Enforcement Procedures
        2. Execution Mechanisms
        3. Asset Location Strategy
        4. Public Policy Defenses
        5. Enforcement Costs and Timeline
        6. Alternative Enforcement Routes
        7. Enforcement Success Probability
        
        Return as JSON with detailed analysis."""
        
        response = await self.call_llm(prompt)
        
        try:
            result = json.loads(response)
        except:
            result = {"raw_analysis": response}
        
        logger.info(f"Enforcement analysis complete")
        return result
