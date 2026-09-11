import logging
from typing import Dict, Any
from abc import ABC, abstractmethod
import openai
from app.config import settings

logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    """Base class for all PIL agents"""
    
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self.client = openai.OpenAI(
            api_key=settings.openai_api_key,
            base_url=settings.openai_base_url
        )
    
    async def call_llm(self, prompt: str, system_prompt: str = None) -> str:
        """Call LLM with prompt"""
        try:
            if system_prompt is None:
                system_prompt = self._get_system_prompt()
            
            response = self.client.chat.completions.create(
                model=settings.openai_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=4000
            )
            
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling LLM in {self.agent_name}: {e}")
            raise
    
    @abstractmethod
    def _get_system_prompt(self) -> str:
        """Get system prompt for this agent"""
        pass
    
    @abstractmethod
    async def analyze(self, **kwargs) -> Dict[str, Any]:
        """Analyze case facts"""
        pass
