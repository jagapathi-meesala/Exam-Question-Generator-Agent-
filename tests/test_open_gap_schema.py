import os
import yaml
import json
import pytest
import jsonschema

def test_agent_yaml_schema_validation():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    agent_yaml_path = os.path.join(base_dir, "agent.yaml")
    
    assert os.path.exists(agent_yaml_path), "agent.yaml is missing"
    
    with open(agent_yaml_path, 'r') as f:
        agent_data = yaml.safe_load(f)
        
    schema_path = "/tmp/opengap/opengap-main/spec/schemas/agent-yaml.schema.json"
    if os.path.exists(schema_path):
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        
        try:
            jsonschema.validate(instance=agent_data, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            pytest.fail(f"agent.yaml schema validation failed: {e.message}")
    else:
        pytest.skip("OpenGAP schema not found locally at /tmp/opengap")

def test_tool_yaml_schema_validation():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    tools_dir = os.path.join(base_dir, "tools")
    schema_path = "/tmp/opengap/opengap-main/spec/schemas/tool.schema.json"
    
    if not os.path.exists(schema_path):
        pytest.skip("OpenGAP schema not found locally at /tmp/opengap")
        
    with open(schema_path, 'r') as f:
        schema = json.load(f)
        
    for file in os.listdir(tools_dir):
        if file.endswith(".yaml"):
            with open(os.path.join(tools_dir, file), 'r') as f:
                tool_data = yaml.safe_load(f)
            try:
                jsonschema.validate(instance=tool_data, schema=schema)
            except jsonschema.exceptions.ValidationError as e:
                pytest.fail(f"Tool {file} schema validation failed: {e.message}")
