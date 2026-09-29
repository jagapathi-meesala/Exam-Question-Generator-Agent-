from typing import Any, Dict
from abc import ABC, abstractmethod
from .agent_contract import AgentContract

class AgentAdapter(ABC):
    """
    Abstract adapter for translating the core agent into different frameworks
    (e.g., OpenGAP runtime, LangChain, AutoGen).
    """

    def __init__(self, agent: AgentContract):
        self.agent = agent

    @abstractmethod
    def export(self) -> Any:
        """Export the agent to the target framework's expected format."""
        pass

    @abstractmethod
    def execute(self, tool_name: str, input_data: Dict[str, Any]) -> Any:
        """Execute the tool in the context of the target framework."""
        pass
