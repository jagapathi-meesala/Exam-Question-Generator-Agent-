from typing import Any, Dict, List
from contracts.tool_contract import ToolContract

class DynamicToolRegistry:
    def __init__(self):
        self._tools: Dict[str, ToolContract] = {}

    def register(self, tool: ToolContract) -> None:
        if not isinstance(tool, ToolContract):
            raise TypeError("Tool must implement ToolContract")
        if tool.name in self._tools:
            raise ValueError(f"Tool '{tool.name}' is already registered.")
        if not tool.name or not isinstance(tool.name, str):
            raise ValueError("Tool name must be a valid string.")
        self._tools[tool.name] = tool

    def get(self, tool_name: str) -> ToolContract:
        if tool_name not in self._tools:
            raise KeyError(f"Tool '{tool_name}' not found in registry.")
        return self._tools[tool_name]

    def list_tools(self) -> List[str]:
        return list(self._tools.keys())

    def execute(self, tool_name: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        tool = self.get(tool_name)
        return tool.execute(input_data)
