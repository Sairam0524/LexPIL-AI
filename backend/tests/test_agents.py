import pytest
from app.agents.characterization_agent import CharacterizationAgent

@pytest.mark.asyncio
async def test_characterization_agent():
    agent = CharacterizationAgent()
    assert agent.agent_name == "CharacterizationAgent"
