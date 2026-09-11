import logging
import json
from typing import Dict, Any
from app.agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)

class RecognitionAgent(BaseAgent):
    """Analyzes recognition of foreign judgments"""
    
    def __init__(self):
        super().__init__("RecognitionAgent")
    
    def _get_system_prompt(self) -> str:
        return """You are an expert in recognizing foreign judgments, decrees, and awards.
        Analyze requirements for recognition under PIL principles and relevant jurisdictions.
        Consider public policy, reciprocity, and procedural requirements.
        Return JSON formatted response."""
    
    async def analyze(self, case_facts: Dict[str, Any], jurisdiction_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze recognition issues"""
        prompt = f"""Analyze foreign judgment recognition issues:
        
        Case Facts: {json.dumps(case_facts, indent=2)}
        Jurisdiction Analysis: {json.dumps(jurisdiction_analysis, indent=2)}
        
        Analyze:
        1. Foreign Judgment Recognition Requirements
        2. Public Policy Considerations
        3. Reciprocity Requirements
        4. Procedural Requirements
        5. Finality Requirements
        6. Recognition Risks and Defenses
        7. Applicable Treaties (New York Convention, etc.)
        
        Return as JSON with detailed analysis."""
        
        response = await self.call_llm(prompt)
        
        try:
            result = json.loads(response)
        except:
            result = {"raw_analysis": response}
        
        logger.info(f"Recognition analysis complete")
        return result
