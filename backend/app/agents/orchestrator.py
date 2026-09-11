import logging
from typing import Dict, Any, List
from app.agents.characterization_agent import CharacterizationAgent
from app.agents.jurisdiction_agent import JurisdictionAgent
from app.agents.choice_of_law_agent import ChoiceOfLawAgent
from app.agents.recognition_agent import RecognitionAgent
from app.agents.enforcement_agent import EnforcementAgent
from app.agents.research_agent import ResearchAgent
from app.agents.treaty_agent import TreatyAgent
from app.agents.citation_agent import CitationAgent
from app.agents.strategy_agent import StrategyAgent

logger = logging.getLogger(__name__)

class AgentOrchestrator:
    """Orchestrates all PIL agents for coordinated legal analysis"""
    
    def __init__(self):
        self.characterization_agent = CharacterizationAgent()
        self.jurisdiction_agent = JurisdictionAgent()
        self.choice_of_law_agent = ChoiceOfLawAgent()
        self.recognition_agent = RecognitionAgent()
        self.enforcement_agent = EnforcementAgent()
        self.research_agent = ResearchAgent()
        self.treaty_agent = TreatyAgent()
        self.citation_agent = CitationAgent()
        self.strategy_agent = StrategyAgent()
    
    async def analyze_case(self, case_facts: Dict[str, Any]) -> Dict[str, Any]:
        """Orchestrate complete case analysis"""
        try:
            logger.info(f"Starting case analysis orchestration")
            
            # Step 1: Characterization
            characterization = await self.characterization_agent.analyze(case_facts)
            logger.info(f"Characterization complete: {characterization.get('dispute_type')}")
            
            # Step 2: Jurisdiction Analysis
            jurisdiction = await self.jurisdiction_agent.analyze(
                case_facts=case_facts,
                dispute_type=characterization.get('dispute_type')
            )
            logger.info(f"Jurisdiction analysis complete")
            
            # Step 3: Choice of Law
            choice_of_law = await self.choice_of_law_agent.analyze(
                case_facts=case_facts,
                dispute_type=characterization.get('dispute_type'),
                potential_jurisdictions=jurisdiction.get('potential_jurisdictions')
            )
            logger.info(f"Choice of law analysis complete")
            
            # Step 4: Treaty Analysis
            treaties = await self.treaty_agent.analyze(
                potential_jurisdictions=jurisdiction.get('potential_jurisdictions')
            )
            logger.info(f"Treaty analysis complete")
            
            # Step 5: Recognition Analysis
            recognition = await self.recognition_agent.analyze(
                case_facts=case_facts,
                jurisdiction_analysis=jurisdiction
            )
            logger.info(f"Recognition analysis complete")
            
            # Step 6: Enforcement Analysis
            enforcement = await self.enforcement_agent.analyze(
                case_facts=case_facts,
                recognition_analysis=recognition
            )
            logger.info(f"Enforcement analysis complete")
            
            # Step 7: Research & Citations
            research = await self.research_agent.analyze(
                dispute_type=characterization.get('dispute_type'),
                jurisdictions=jurisdiction.get('potential_jurisdictions'),
                choice_of_law=choice_of_law.get('applicable_law')
            )
            logger.info(f"Research complete")
            
            # Step 8: Citation Analysis
            citations = await self.citation_agent.analyze(
                research_results=research
            )
            logger.info(f"Citation analysis complete")
            
            # Step 9: Strategy Generation
            strategy = await self.strategy_agent.analyze(
                case_facts=case_facts,
                characterization=characterization,
                jurisdiction=jurisdiction,
                choice_of_law=choice_of_law,
                recognition=recognition,
                enforcement=enforcement,
                research=research
            )
            logger.info(f"Strategy generation complete")
            
            # Compile comprehensive analysis
            analysis = {
                "characterization": characterization,
                "jurisdiction": jurisdiction,
                "choice_of_law": choice_of_law,
                "treaties": treaties,
                "recognition": recognition,
                "enforcement": enforcement,
                "research": research,
                "citations": citations,
                "strategy": strategy,
            }
            
            logger.info("Case analysis orchestration complete")
            return analysis
            
        except Exception as e:
            logger.error(f"Error in orchestration: {e}", exc_info=True)
            raise
