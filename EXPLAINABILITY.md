# Explainability

- **Non-LLM Nature**: This agent uses no machine learning models. Every text output is generated through standard string templating based directly on the provided topic or source input.
- **Source-Dependent Behavior**: Question quality is purely dependent on the structure of the input topic.
- **Non-Authoritative**: Generated content is educational scaffold material. The agent does NOT retrieve external knowledge.
- **classify-difficulty**:
  - Score = `(expected_answer_complexity * 1.5) + (number_of_concepts * 2.0) + (number_of_steps * 1.0)`
  - Thresholds: Score < 10 (Easy), Score < 20 (Medium), >= 20 (Hard).
- **Validation Rules**: `validate-question-set` uses standard JSON and set-logic deduplication.
- **Deterministic Behavior**: All loops, assignments, and logic branching behave exactly the same given identical inputs. No `random` modules are used.
