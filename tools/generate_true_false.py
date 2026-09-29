import jsonschema
from typing import Any, Dict
from contracts.tool_contract import ToolContract

class GenerateTrueFalseTool(ToolContract):
    @property
    def name(self) -> str:
        return "generate-true-false"

    @property
    def description(self) -> str:
        return "Generate deterministic true/false questions."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
                "source_text": {"type": "string"},
                "number_of_questions": {"type": "integer", "minimum": 1, "maximum": 50},
                "difficulty": {"type": "string", "enum": ["easy", "medium", "hard"]}
            },
            "required": ["topic", "number_of_questions", "difficulty"]
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
                            "statement": {"type": "string"},
                            "answer": {"type": "boolean"},
                            "explanation": {"type": "string"},
                            "difficulty": {"type": "string"},
                            "topic": {"type": "string"}
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
        
        questions = []
        for i in range(1, num_q + 1):
            is_true = (i % 2 == 0) # Deterministic assignment
            questions.append({
                "statement": f"{topic} is a relevant concept. (Instance {i})",
                "answer": is_true,
                "explanation": f"This statement is {'true' if is_true else 'false'} based on standard rules for {topic}.",
                "difficulty": diff,
                "topic": topic
            })
            
        return {"questions": questions}
