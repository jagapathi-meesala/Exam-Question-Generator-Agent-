import jsonschema
from typing import Any, Dict
from contracts.tool_contract import ToolContract

class GenerateLongAnswerTool(ToolContract):
    @property
    def name(self) -> str:
        return "generate-long-answer"

    @property
    def description(self) -> str:
        return "Generate descriptive/long-answer examination questions."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
                "source_text": {"type": "string"},
                "number_of_questions": {"type": "integer", "minimum": 1, "maximum": 50},
                "difficulty": {"type": "string", "enum": ["easy", "medium", "hard"]},
                "expected_marks": {"type": "integer", "minimum": 1}
            },
            "required": ["topic", "number_of_questions", "difficulty", "expected_marks"]
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
                            "expected_answer_points": {"type": "array", "items": {"type": "string"}},
                            "difficulty": {"type": "string"},
                            "topic": {"type": "string"},
                            "marks": {"type": "integer"}
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
        marks = input_data["expected_marks"]
        
        questions = []
        for i in range(1, num_q + 1):
            questions.append({
                "question": f"Discuss in detail the implications of {topic} (Part {i}).",
                "expected_answer_points": [
                    f"Point 1 about {topic}",
                    f"Point 2 elaborating on {topic}",
                    f"Conclusion regarding {topic}"
                ],
                "difficulty": diff,
                "topic": topic,
                "marks": marks
            })
            
        return {"questions": questions}
