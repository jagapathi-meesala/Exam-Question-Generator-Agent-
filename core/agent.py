from typing import Any, Dict
from contracts.agent_contract import AgentContract
from contracts.tool_contract import ToolContract
from core.registry import DynamicToolRegistry

class AgentCore(AgentContract):
    def __init__(self, name: str = "Exam Question Generator Agent", version: str = "1.0.0"):
        self._name = name
        self._version = version
        self.registry = DynamicToolRegistry()

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version

    @property
    def metadata(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "version": self.version,
            "description": "Agent for generating and analyzing examination questions from structured input deterministically.",
            "tools": self.registry.list_tools()
        }

    def register_tool(self, tool: ToolContract) -> None:
        self.registry.register(tool)

    def execute_tool(self, tool_name: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a tool safely through the registry.
        """
        return self.registry.execute(tool_name, input_data)
