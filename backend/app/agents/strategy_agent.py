import logging
import json
from typing import Dict, Any
from app.agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)

class StrategyAgent(BaseAgent):
    """Generates litigation strategy"""
    
    def __init__(self):
        super().__init__("StrategyAgent")
    
    def _get_system_prompt(self) -> str:
        return """You are a strategic PIL litigation expert.
        Generate comprehensive litigation strategies based on complete case analysis.
        Provide tactical recommendations and risk assessments.
        Return JSON formatted response."""
    
    async def analyze(self, case_facts: Dict[str, Any], characterization: Dict[str, Any],
                     jurisdiction: Dict[str, Any], choice_of_law: Dict[str, Any],
                     recognition: Dict[str, Any], enforcement: Dict[str, Any],
                     research: Dict[str, Any]) -> Dict[str, Any]:
        """Generate litigation strategy"""
        prompt = f"""Generate comprehensive PIL litigation strategy:
        
        Case Facts: {json.dumps(case_facts, indent=2)}
        Characterization: {json.dumps(characterization, indent=2)}
        Jurisdiction: {json.dumps(jurisdiction, indent=2)}
        Choice of Law: {json.dumps(choice_of_law, indent=2)}
        Recognition: {json.dumps(recognition, indent=2)}
        Enforcement: {json.dumps(enforcement, indent=2)}
        Research: {json.dumps(research, indent=2)}
        
        Recommend:
        1. Optimal Jurisdiction Selection
        2. Forum Shopping Considerations
        3. Tactical Moves
        4. Risk Mitigation Strategies
        5. Evidence Gathering Strategy
        6. Enforcement Strategy
        7. Cost-Benefit Analysis
        8. Timeline and Milestones
        9. Alternative Dispute Resolution
        10. Success Probability Assessment
        
        Return as JSON with detailed strategy."""
        
        response = await self.call_llm(prompt)
        
        try:
            result = json.loads(response)
        except:
            result = {"raw_analysis": response}
        
        logger.info(f"Strategy generation complete")
        return result
