import jsonschema
from typing import Any, Dict
from contracts.tool_contract import ToolContract

class ClassifyDifficultyTool(ToolContract):
    @property
    def name(self) -> str:
        return "classify-difficulty"

    @property
    def description(self) -> str:
        return "Classify questions into easy, medium, or hard using an explicit deterministic rule."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "question_text": {"type": "string"},
                "expected_answer_complexity": {"type": "integer", "minimum": 1, "maximum": 10},
                "number_of_concepts": {"type": "integer", "minimum": 1, "maximum": 10},
                "number_of_steps": {"type": "integer", "minimum": 1, "maximum": 10}
            },
            "required": ["question_text", "expected_answer_complexity", "number_of_concepts", "number_of_steps"]
        }

    @property
    def output_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "difficulty": {"type": "string", "enum": ["easy", "medium", "hard"]},
                "contributing_factors": {"type": "object"},
                "calculation_explanation": {"type": "string"}
            }
        }

    def validate_input(self, input_data: Dict[str, Any]) -> None:
        try:
            jsonschema.validate(instance=input_data, schema=self.input_schema)
        except jsonschema.exceptions.ValidationError as e:
            raise ValueError(f"Invalid input: {e.message}")

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        self.validate_input(input_data)
        
        complexity = input_data["expected_answer_complexity"]
        concepts = input_data["number_of_concepts"]
        steps = input_data["number_of_steps"]
        
        # Deterministic formula
        score = (complexity * 1.5) + (concepts * 2.0) + (steps * 1.0)
        
        if score < 10:
            difficulty = "easy"
        elif score < 20:
            difficulty = "medium"
        else:
            difficulty = "hard"
            
        return {
            "difficulty": difficulty,
            "contributing_factors": {
                "complexity_score": complexity * 1.5,
                "concepts_score": concepts * 2.0,
                "steps_score": steps * 1.0,
                "total_score": score
            },
            "calculation_explanation": f"Score calculated as (complexity*1.5 + concepts*2.0 + steps*1.0) = {score}. Thresholds: <10 easy, <20 medium, else hard."
        }
