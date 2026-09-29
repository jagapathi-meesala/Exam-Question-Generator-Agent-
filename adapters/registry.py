from typing import Dict, Type
from contracts.adapter import AgentAdapter

class AdapterRegistry:
    def __init__(self):
        self._adapters: Dict[str, Type[AgentAdapter]] = {}

    def register(self, name: str, adapter_cls: Type[AgentAdapter]) -> None:
        if name in self._adapters:
            raise ValueError(f"Adapter {name} is already registered.")
        self._adapters[name] = adapter_cls

    def get(self, name: str) -> Type[AgentAdapter]:
        if name not in self._adapters:
            raise KeyError(f"Adapter {name} not found.")
        return self._adapters[name]
