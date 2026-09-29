import pytest
from tools.generate_mcq import GenerateMCQTool

def test_security_invalid_input():
    tool = GenerateMCQTool()
    # Missing required fields
    with pytest.raises(ValueError):
        tool.execute({"topic": "Math"})
    
    # Invalid type
    with pytest.raises(ValueError):
        tool.execute({
            "topic": "Math",
            "number_of_questions": "two", # Should be integer
            "difficulty": "easy",
            "options_count": 4
        })

def test_security_out_of_bounds():
    tool = GenerateMCQTool()
    with pytest.raises(ValueError):
        tool.execute({
            "topic": "Math",
            "number_of_questions": 100, # Max is 50
            "difficulty": "easy",
            "options_count": 4
        })
