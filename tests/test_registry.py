import pytest
from core.registry import DynamicToolRegistry
from tools.generate_mcq import GenerateMCQTool

def test_registry_registration():
    registry = DynamicToolRegistry()
    tool = GenerateMCQTool()
    registry.register(tool)
    assert tool.name in registry.list_tools()
    assert registry.get(tool.name) == tool

def test_duplicate_registration():
    registry = DynamicToolRegistry()
    tool = GenerateMCQTool()
    registry.register(tool)
    with pytest.raises(ValueError):
        registry.register(tool)

def test_missing_tool():
    registry = DynamicToolRegistry()
    with pytest.raises(KeyError):
        registry.get("non-existent-tool")
