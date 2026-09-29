import jsonschema
from typing import Any, Dict
from collections import Counter
from contracts.tool_contract import ToolContract

class AnalyzeQuestionSetTool(ToolContract):
    @property
    def name(self) -> str:
        return "analyze-question-set"

    @property
    def description(self) -> str:
        return "Analyze an existing structured question set."

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
                            "type": {"type": "string"},
                            "difficulty": {"type": "string"},
                            "topic": {"type": "string"},
                            "marks": {"type": "integer"}
                        }
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
                "total_questions": {"type": "integer"},
                "question_type_distribution": {"type": "object"},
                "difficulty_distribution": {"type": "object"},
                "topic_distribution": {"type": "object"},
                "total_marks": {"type": "integer"},
                "average_marks": {"type": "number"},
                "duplicate_count": {"type": "integer"},
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
        total_questions = len(questions)
        
        type_dist = Counter()
        diff_dist = Counter()
        topic_dist = Counter()
        total_marks = 0
        questions_with_marks = 0
        seen_ids = set()
        duplicate_count = 0
        
        for q in questions:
            q_id = q.get("id")
            if q_id:
                if q_id in seen_ids:
                    duplicate_count += 1
                seen_ids.add(q_id)
            
            q_type = q.get("type", "unknown")
            diff = q.get("difficulty", "unknown")
            topic = q.get("topic", "unknown")
            marks = q.get("marks")
            
            type_dist[q_type] += 1
            diff_dist[diff] += 1
            topic_dist[topic] += 1
            
            if marks is not None:
                total_marks += marks
                questions_with_marks += 1
                
        avg_marks = (total_marks / questions_with_marks) if questions_with_marks > 0 else 0.0
        
        return {
            "total_questions": total_questions,
            "question_type_distribution": dict(type_dist),
            "difficulty_distribution": dict(diff_dist),
            "topic_distribution": dict(topic_dist),
            "total_marks": total_marks,
            "average_marks": round(avg_marks, 2),
            "duplicate_count": duplicate_count,
            "validation_summary": f"Analyzed {total_questions} questions, found {duplicate_count} duplicates."
        }
