import logging
import json
from typing import Dict, Any
from app.agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)

class CitationAgent(BaseAgent):
    """Analyzes and formats citations"""
    
    def __init__(self):
        super().__init__("CitationAgent")
    
    def _get_system_prompt(self) -> str:
        return """You are an expert in legal citation and authority analysis.
        Analyze citation relationships, precedent weight, and relevance.
        Return JSON formatted response with proper citations."""
    
    async def analyze(self, research_results: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze citations"""
        prompt = f"""Analyze citation relationships and authority:
        
        Research Results: {json.dumps(research_results, indent=2)}
        
        Analyze:
        1. Citation Hierarchy
        2. Precedent Weight
        3. Binding vs Persuasive Authority
        4. Citation Relationships
        5. Distinguishing Factors
        6. Supporting vs Opposing Authority
        7. Proper Citation Format
        
        Return as JSON with detailed citation analysis."""
        
        response = await self.call_llm(prompt)
        
        try:
            result = json.loads(response)
        except:
            result = {"raw_analysis": response}
        
        logger.info(f"Citation analysis complete")
        return result
