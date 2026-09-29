import pytest
from core.agent import AgentCore
from tools.generate_mcq import GenerateMCQTool
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_agent_initialization():
    agent = AgentCore()
    assert agent.name == "Exam Question Generator Agent"
    assert agent.version == "1.0.0"

def test_agent_metadata():
    agent = AgentCore()
    meta = agent.metadata
    assert "name" in meta
    assert "version" in meta
    assert "tools" in meta
    assert isinstance(meta["tools"], list)
