import logging
from typing import List
import re

logger = logging.getLogger(__name__)

class CitationExtractor:
    """Extracts citations from legal documents"""
    
    @staticmethod
    def extract_citations(content: str) -> List[str]:
        """Extract case citations from text"""
        citations = []
        try:
            # Indian citations (e.g., "2023 SCC Online 1234")
            indian_pattern = r'\d{4}\s+(?:SCC|SCR|SCA|SCC\s+Online)\s+\d+'
            citations.extend(re.findall(indian_pattern, content))
            
            # UK citations (e.g., "[2023] EWHC 123")
            uk_pattern = r'\[\d{4}\]\s+(?:EWHC|EWCA|UKSC|BAILII)\s+\d+'
            citations.extend(re.findall(uk_pattern, content))
            
            # US citations (e.g., "123 F.3d 456")
            us_pattern = r'\d+\s+(?:F\.|U\.S\.|S\.Ct\.|L\.Ed)'
            citations.extend(re.findall(us_pattern, content))
            
            logger.info(f"Extracted {len(citations)} citations")
        except Exception as e:
            logger.error(f"Error extracting citations: {e}")
        
        return citations
    
    @staticmethod
    def extract_statutes(content: str) -> List[str]:
        """Extract statute references"""
        statutes = []
        try:
            # Generic statute pattern
            statute_pattern = r'(?:Section|§|Article|Art\.)(\s+\d+(?:\.\d+)*(?:\([a-z]+\))?)\.?'
            statutes.extend(re.findall(statute_pattern, content, re.IGNORECASE))
            
            logger.info(f"Extracted {len(statutes)} statute references")
        except Exception as e:
            logger.error(f"Error extracting statutes: {e}")
        
        return statutes
    
    @staticmethod
    def extract_treaties(content: str) -> List[str]:
        """Extract treaty references"""
        treaties = []
        try:
            # Treaty pattern
            treaty_pattern = r'(?:Convention|Treaty|Protocol|Agreement)\s+(?:on|for|concerning)\s+([^,\.]+)'
            treaties.extend(re.findall(treaty_pattern, content, re.IGNORECASE))
            
            logger.info(f"Extracted {len(treaties)} treaty references")
        except Exception as e:
            logger.error(f"Error extracting treaties: {e}")
        
        return treaties
