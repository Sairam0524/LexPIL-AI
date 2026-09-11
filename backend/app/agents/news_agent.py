import logging
import json
from typing import Dict, Any, List
from app.agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)

class NewsAgent(BaseAgent):
    """Monitors legal news and updates"""
    
    def __init__(self):
        super().__init__("NewsAgent")
    
    def _get_system_prompt(self) -> str:
        return """You are a legal news analyst specializing in PIL developments.
        Analyze legal news for impact on PIL practice and provide summaries.
        Return JSON formatted response."""
    
    async def analyze(self, news_items: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze legal news"""
        prompt = f"""Analyze these legal news items for PIL significance:
        
        News Items: {json.dumps(news_items, indent=2)}
        
        Analyze:
        1. PIL Impact
        2. Jurisdiction Affected
        3. Precedent Value
        4. Practice Implications
        5. Risk Alerts
        6. Opportunity Identification
        
        Return as JSON with detailed analysis."""
        
        response = await self.call_llm(prompt)
        
        try:
            result = json.loads(response)
        except:
            result = {"raw_analysis": response}
        
        logger.info(f"News analysis complete")
        return result
