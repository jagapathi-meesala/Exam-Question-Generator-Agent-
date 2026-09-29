from typing import Any, Dict
from contracts.adapter import AgentAdapter
from core.agent import AgentCore

class PortableAdapter(AgentAdapter):
    """
    A simple portable adapter that allows the agent to be embedded
    in arbitrary Python applications or wrapped by web frameworks without modifying
    the core business logic.
    """

    def export(self) -> Dict[str, Any]:
        return {
            "type": "portable_agent",
            "metadata": self.agent.metadata,
            "callable_interface": "execute",
        }

    def execute(self, tool_name: str, input_data: Dict[str, Any]) -> Any:
        return self.agent.execute_tool(tool_name, input_data)
