import jsonschema
from typing import Any, Dict
from contracts.tool_contract import ToolContract

class GenerateShortAnswerTool(ToolContract):
    @property
    def name(self) -> str:
        return "generate-short-answer"

    @property
    def description(self) -> str:
        return "Generate short-answer questions from structured topic/content input."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
                "source_text": {"type": "string"},
                "number_of_questions": {"type": "integer", "minimum": 1, "maximum": 50},
                "difficulty": {"type": "string", "enum": ["easy", "medium", "hard"]},
                "expected_answer_length": {"type": "integer", "minimum": 1, "maximum": 500}
            },
            "required": ["topic", "number_of_questions", "difficulty", "expected_answer_length"]
        }

    @property
    def output_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "questions": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "question": {"type": "string"},
                            "expected_answer": {"type": "string"},
                            "difficulty": {"type": "string"},
                            "topic": {"type": "string"},
                            "explanation": {"type": "string"}
                        }
                    }
                }
            }
        }

    def validate_input(self, input_data: Dict[str, Any]) -> None:
        try:
            jsonschema.validate(instance=input_data, schema=self.input_schema)
        except jsonschema.exceptions.ValidationError as e:
            raise ValueError(f"Invalid input: {e.message}")

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        self.validate_input(input_data)
        
        topic = input_data["topic"]
        num_q = input_data["number_of_questions"]
        diff = input_data["difficulty"]
        length = input_data["expected_answer_length"]
        
        questions = []
        for i in range(1, num_q + 1):
            questions.append({
                "question": f"Briefly explain {topic} (Concept {i}).",
                "expected_answer": f"Expected answer covering {topic} within {length} characters.",
                "difficulty": diff,
                "topic": topic,
                "explanation": f"Generated based on the provided rule template."
            })
            
        return {"questions": questions}
