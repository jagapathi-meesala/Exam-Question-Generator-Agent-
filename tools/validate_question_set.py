import jsonschema
from typing import Any, Dict
from contracts.tool_contract import ToolContract

class ValidateQuestionSetTool(ToolContract):
    @property
    def name(self) -> str:
        return "validate-question-set"

    @property
    def description(self) -> str:
        return "Validate a structured examination question set."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "questions": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "type": {"type": "string", "enum": ["mcq", "short-answer", "long-answer", "true-false"]},
                            "question": {"type": "string"},
                            "difficulty": {"type": "string", "enum": ["easy", "medium", "hard"]}
                        },
                        "required": ["id", "type", "question", "difficulty"]
                    }
                }
            },
            "required": ["questions"]
        }

    @property
    def output_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "valid": {"type": "boolean"},
                "errors": {"type": "array", "items": {"type": "string"}},
                "warnings": {"type": "array", "items": {"type": "string"}},
                "duplicate_questions": {"type": "array", "items": {"type": "string"}},
                "invalid_questions": {"type": "array", "items": {"type": "string"}},
                "validation_summary": {"type": "string"}
            }
        }

    def validate_input(self, input_data: Dict[str, Any]) -> None:
        try:
            jsonschema.validate(instance=input_data, schema=self.input_schema)
        except jsonschema.exceptions.ValidationError as e:
            raise ValueError(f"Invalid input: {e.message}")

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        self.validate_input(input_data)
        
        questions = input_data["questions"]
        errors = []
        warnings = []
        duplicate_ids = []
        invalid_ids = []
        seen_ids = set()
        
        for idx, q in enumerate(questions):
            q_id = q.get("id")
            
            if q_id in seen_ids:
                errors.append(f"Duplicate question ID found: {q_id}")
                duplicate_ids.append(q_id)
            seen_ids.add(q_id)
            
            if not q.get("question") or str(q.get("question")).strip() == "":
                invalid_ids.append(q_id)
                errors.append(f"Question {q_id} has empty question text.")
                
            q_type = q.get("type")
            if q_type == "mcq" and "options" not in q:
                warnings.append(f"MCQ {q_id} has no options defined.")
                
        is_valid = len(errors) == 0
        
        return {
            "valid": is_valid,
            "errors": errors,
            "warnings": warnings,
            "duplicate_questions": list(set(duplicate_ids)),
            "invalid_questions": list(set(invalid_ids)),
            "validation_summary": f"Validation finished with {len(errors)} errors and {len(warnings)} warnings."
        }
