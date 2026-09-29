# Exam Question Generator Agent

## 1. Overview
The Exam Question Generator Agent is a deterministic, framework-independent agent designed for the HiDevs Agent Passport / OpenGAP ecosystem. It generates, validates, and analyzes educational questions without relying on LLMs or non-deterministic ML models.

## 2. Features
- **Deterministic Generation**: Generates MCQs, short answers, long answers, and true/false questions deterministically.
- **Rule-Based Difficulty**: Classifies question difficulty using explicit mathematical thresholds.
- **Validation**: Strict validation of question sets (checking missing IDs, empty texts, duplicates).
- **Analysis**: Calculates question type distributions, difficulty distributions, and marks statistics.
- **OpenGAP Compliant**: Adheres to the latest OpenGAP agent and tool schemas.
- **Portable Architecture**: Can be adapted into LangChain, AutoGen, or custom runtimes via the Adapter pattern.

## 3. Architecture
The agent is built with modularity in mind:
- **Core**: Contains `AgentCore` and `DynamicToolRegistry`.
- **Contracts**: Interface definitions (`AgentContract`, `ToolContract`, `AgentAdapter`).
- **Tools**: Each capability is encapsulated in a separate executable Python file and OpenGAP YAML manifest.
- **Adapters**: Framework translations like `PortableAdapter`.

## 4. Tools
- `generate-mcq`
- `generate-short-answer`
- `generate-long-answer`
- `generate-true-false`
- `classify-difficulty`
- `validate-question-set`
- `analyze-question-set`

## 5. Tool Input/Output Examples
**Input to `generate-mcq`:**
```json
{
  "topic": "Photosynthesis",
  "number_of_questions": 2,
  "difficulty": "medium",
  "options_count": 4
}
```
**Output from `generate-mcq`:**
```json
{
  "questions": [
    {
      "question": "What is a key concept of Photosynthesis (Part 1) based on 'Photosynthesis'? (Generated template)",
      "options": ["Option 1 for Photosynthesis", "Option 2 for Photosynthesis", "Option 3 for Photosynthesis", "Option 4 for Photosynthesis"],
      "correct_answer": "Option 1 for Photosynthesis",
      "difficulty": "medium",
      "topic": "Photosynthesis",
      "explanation": "Derived deterministically from topic: Photosynthesis."
    }
  ]
}
```

## 6. Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 7. Configuration
Configuration uses environment variables (see `.env.example`).
No hardcoded API keys or secrets exist.

## 8. Running Tests
```bash
pytest -q
```

## 9. Local Validation
You can run the schema validation test suite:
```bash
pytest tests/test_open_gap_schema.py
```

## 10. OpenGAP Compliance
The project is built specifically following the OpenGAP schema definitions.

## 11. Security
The agent operates completely deterministically. It executes no arbitrary bash commands, no `eval()`, and avoids subprocess injection vectors. All tool inputs are validated via `jsonschema` before execution.

## 12. Portability
Uses `AgentAdapter` abstractions to ensure the agent logic remains untethered to heavy dependencies like LangChain.

## 13. Limitations
- Does not use an LLM.
- Output text is generated from deterministic templates.
- Factual correctness relies entirely on the provided inputs/source material.

## 14. Project Structure
See repository layout.

## 15. Extension Guide
To add a new tool:
1. Create `tools/<tool-name>.py` extending `ToolContract`.
2. Create `tools/<tool-name>.yaml` describing the OpenGAP manifest.
3. Update `agent.yaml` to include `<tool-name>` in the `tools` array.
