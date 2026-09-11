from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict, Any
import logging
from app.agents.orchestrator import AgentOrchestrator
from app.database import SessionLocal

logger = logging.getLogger(__name__)
router = APIRouter()

class CaseAnalysisRequest(BaseModel):
    party1: str
    party2: str
    party1_jurisdiction: str
    party2_jurisdiction: str
    dispute_subject: str
    facts: str
    additional_context: Dict[str, Any] = {}

class CaseAnalysisResponse(BaseModel):
    analysis_id: str
    characterization: Dict[str, Any]
    jurisdiction: Dict[str, Any]
    choice_of_law: Dict[str, Any]
    treaties: Dict[str, Any]
    recognition: Dict[str, Any]
    enforcement: Dict[str, Any]
    research: Dict[str, Any]
    citations: Dict[str, Any]
    strategy: Dict[str, Any]

orchestrator = AgentOrchestrator()

@router.post("/analyze", response_model=Dict[str, Any])
async def analyze_case(request: CaseAnalysisRequest):
    """Analyze a legal case using multi-agent system"""
    try:
        case_facts = {
            "party1": request.party1,
            "party2": request.party2,
            "party1_jurisdiction": request.party1_jurisdiction,
            "party2_jurisdiction": request.party2_jurisdiction,
            "dispute_subject": request.dispute_subject,
            "facts": request.facts,
            **request.additional_context
        }
        
        analysis = await orchestrator.analyze_case(case_facts)
        
        logger.info(f"Case analysis completed for {request.party1} vs {request.party2}")
        
        return {
            "status": "success",
            "analysis": analysis
        }
    except Exception as e:
        logger.error(f"Error analyzing case: {e}")
        raise HTTPException(status_code=500, detail=str(e))
