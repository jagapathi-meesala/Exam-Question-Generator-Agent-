from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod

class ToolContract(ABC):
    """
    Contract for all tools in the Exam Question Generator Agent ecosystem.
    Tools must be deterministic and validate their inputs/outputs.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the unique name of the tool."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Return the description of what the tool does."""
        pass

    @property
    @abstractmethod
    def input_schema(self) -> Dict[str, Any]:
        """Return the JSON schema for the input."""
        pass

    @property
    @abstractmethod
    def output_schema(self) -> Dict[str, Any]:
        """Return the JSON schema for the output."""
        pass

    @abstractmethod
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the tool with the provided input data.
        Must validate input and raise ValueError for invalid data.
        Must return deterministic output.
        """
        pass

    def validate_input(self, input_data: Dict[str, Any]) -> None:
        """Base implementation for input validation (optional to override if using jsonschema)."""
        pass
