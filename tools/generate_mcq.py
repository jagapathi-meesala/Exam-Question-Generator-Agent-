import jsonschema
from typing import Any, Dict
from contracts.tool_contract import ToolContract

class GenerateMCQTool(ToolContract):
    @property
    def name(self) -> str:
        return "generate-mcq"

    @property
    def description(self) -> str:
        return "Generate deterministic multiple-choice questions from structured input."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
                "source_text": {"type": "string"},
                "number_of_questions": {"type": "integer", "minimum": 1, "maximum": 50},
                "difficulty": {"type": "string", "enum": ["easy", "medium", "hard"]},
                "options_count": {"type": "integer", "minimum": 2, "maximum": 6},
                "include_answers": {"type": "boolean"}
            },
            "required": ["topic", "number_of_questions", "difficulty", "options_count"]
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
                            "options": {"type": "array", "items": {"type": "string"}},
                            "correct_answer": {"type": "string"},
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
        opts = input_data["options_count"]
        source = input_data.get("source_text", "")
        
        questions = []
        for i in range(1, num_q + 1):
            base_text = source[:50] if source else topic
            question_text = f"What is a key concept of {topic} (Part {i}) based on '{base_text}'? (Generated template)"
            
            options = [f"Option {j} for {topic}" for j in range(1, opts + 1)]
            correct_answer = options[0]  # Deterministic dummy logic
            
            q_obj = {
                "question": question_text,
                "options": options,
                "correct_answer": correct_answer if input_data.get("include_answers", True) else None,
                "difficulty": diff,
                "topic": topic,
                "explanation": f"Derived deterministically from topic: {topic}."
            }
            questions.append(q_obj)
            
        return {"questions": questions}
