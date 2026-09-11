import logging
import json
from typing import Dict, Any, List
from app.agents.base_agent import BaseAgent
from app.database import chroma_client

logger = logging.getLogger(__name__)

class ResearchAgent(BaseAgent):
    """Retrieves supporting legal authorities"""
    
    def __init__(self):
        super().__init__("ResearchAgent")
    
    def _get_system_prompt(self) -> str:
        return """You are an expert legal researcher specializing in PIL.
        Recommend relevant case law, statutes, and principles based on analysis.
        Return JSON formatted response with citations."""
    
    async def analyze(self, dispute_type: str, jurisdictions: List[str], 
                     choice_of_law: Dict[str, Any]) -> Dict[str, Any]:
        """Research applicable authorities"""
        
        # Query ChromaDB for relevant authorities
        try:
            collection = chroma_client.get_collection()
            query = f"{dispute_type} {' '.join(jurisdictions)}"
            results = collection.query(
                query_texts=[query],
                n_results=10
            )
            
            authorities = results.get('documents', [[]])[0] if results.get('documents') else []
        except Exception as e:
            logger.error(f"Error querying ChromaDB: {e}")
            authorities = []
        
        prompt = f"""Identify relevant authorities for this PIL case:
        
        Dispute Type: {dispute_type}
        Relevant Jurisdictions: {json.dumps(jurisdictions, indent=2)}
        Choice of Law: {json.dumps(choice_of_law, indent=2)}
        Retrieved Authorities: {authorities}
        
        Recommend:
        1. Most Relevant Cases
        2. Key Statutes
        3. Applicable Principles
        4. Treaty Provisions
        5. Secondary Sources
        
        Return as JSON with detailed recommendations."""
        
        response = await self.call_llm(prompt)
        
        try:
            result = json.loads(response)
        except:
            result = {"raw_analysis": response, "retrieved_authorities": authorities}
        
        logger.info(f"Research analysis complete")
        return result
