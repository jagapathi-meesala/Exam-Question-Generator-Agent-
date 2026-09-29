from typing import Any, Dict, List
from abc import ABC, abstractmethod
from .tool_contract import ToolContract

class AgentContract(ABC):
    """
    Contract for the Exam Question Generator Agent.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        pass

    @property
    @abstractmethod
    def metadata(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def register_tool(self, tool: ToolContract) -> None:
        pass

    @abstractmethod
    def execute_tool(self, tool_name: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        pass
