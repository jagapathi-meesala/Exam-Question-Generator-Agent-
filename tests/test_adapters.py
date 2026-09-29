import pytest
from core.agent import AgentCore
from tools.generate_mcq import GenerateMCQTool
from adapters.portable_adapter import PortableAdapter

def test_portable_adapter():
    agent = AgentCore()
    tool = GenerateMCQTool()
    agent.register_tool(tool)
    
    adapter = PortableAdapter(agent)
    export_data = adapter.export()
    
    assert export_data["type"] == "portable_agent"
    assert export_data["metadata"]["name"] == "Exam Question Generator Agent"
    
    result = adapter.execute("generate-mcq", {
        "topic": "Math",
        "number_of_questions": 1,
        "difficulty": "easy",
        "options_count": 4
    })
    
    assert len(result["questions"]) == 1
