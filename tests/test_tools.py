import pytest
from tools.generate_mcq import GenerateMCQTool
from tools.generate_short_answer import GenerateShortAnswerTool
from tools.generate_long_answer import GenerateLongAnswerTool
from tools.generate_true_false import GenerateTrueFalseTool
from tools.classify_difficulty import ClassifyDifficultyTool
from tools.validate_question_set import ValidateQuestionSetTool
from tools.analyze_question_set import AnalyzeQuestionSetTool

def test_mcq_generation():
    tool = GenerateMCQTool()
    input_data = {
        "topic": "Biology",
        "number_of_questions": 2,
        "difficulty": "medium",
        "options_count": 4
    }
    result = tool.execute(input_data)
    assert len(result["questions"]) == 2
    assert len(result["questions"][0]["options"]) == 4

def test_short_answer_generation():
    tool = GenerateShortAnswerTool()
    input_data = {
        "topic": "History",
        "number_of_questions": 1,
        "difficulty": "easy",
        "expected_answer_length": 100
    }
    result = tool.execute(input_data)
    assert len(result["questions"]) == 1
    assert result["questions"][0]["difficulty"] == "easy"

def test_long_answer_generation():
    tool = GenerateLongAnswerTool()
    input_data = {
        "topic": "Physics",
        "number_of_questions": 1,
        "difficulty": "hard",
        "expected_marks": 10
    }
    result = tool.execute(input_data)
    assert len(result["questions"]) == 1
    assert result["questions"][0]["marks"] == 10
    assert len(result["questions"][0]["expected_answer_points"]) == 3

def test_true_false_generation():
    tool = GenerateTrueFalseTool()
    input_data = {
        "topic": "Chemistry",
        "number_of_questions": 2,
        "difficulty": "easy"
    }
    result = tool.execute(input_data)
    assert len(result["questions"]) == 2
    assert isinstance(result["questions"][0]["answer"], bool)

def test_classify_difficulty():
    tool = ClassifyDifficultyTool()
    input_data = {
        "question_text": "What is 2+2?",
        "expected_answer_complexity": 1,
        "number_of_concepts": 1,
        "number_of_steps": 1
    }
    result = tool.execute(input_data)
    assert result["difficulty"] == "easy"

def test_validate_question_set():
    tool = ValidateQuestionSetTool()
    input_data = {
        "questions": [
            {"id": "q1", "type": "mcq", "question": "Q1", "difficulty": "easy", "options": []},
            {"id": "q1", "type": "mcq", "question": "Q2", "difficulty": "easy"}
        ]
    }
    result = tool.execute(input_data)
    assert result["valid"] is False
    assert "q1" in result["duplicate_questions"]

def test_analyze_question_set():
    tool = AnalyzeQuestionSetTool()
    input_data = {
        "questions": [
            {"id": "q1", "type": "mcq", "difficulty": "easy", "topic": "Math", "marks": 5},
            {"id": "q2", "type": "mcq", "difficulty": "easy", "topic": "Math", "marks": 5}
        ]
    }
    result = tool.execute(input_data)
    assert result["total_questions"] == 2
    assert result["total_marks"] == 10
    assert result["average_marks"] == 5.0
