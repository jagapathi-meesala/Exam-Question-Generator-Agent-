# Explainability

## 1. Agent Purpose

The Exam Question Generator Agent is a deterministic, framework-independent
agent for generating and analyzing examination questions.

It accepts structured educational inputs and produces structured question
outputs using explicit deterministic rules.

The agent does not use an LLM, external knowledge retrieval, or probabilistic
model for its core behavior.

---

## 2. Decision and Processing Flow

The agent follows this general flow:

Input
→ Input validation
→ Tool selection
→ Deterministic processing
→ Output validation
→ Structured result

Each tool has a defined contract describing its inputs, outputs, and expected
behavior.

The agent does not autonomously select undocumented actions or access
undeclared external services.

---

## 3. Explainability of Question Generation

### generate-mcq

The tool generates multiple-choice questions from the supplied input.

The generated question content is derived from the provided topic/source
material and deterministic templates.

The tool produces:

- question text
- answer options
- correct answer
- explanation where supported by the tool contract
- requested difficulty or metadata

No external knowledge is introduced by the agent.

### generate-short-answer

The tool generates short-answer questions using deterministic templates
based on the supplied topic or source input.

### generate-long-answer

The tool generates long-answer questions using deterministic templates
based on the supplied topic or source input.

### generate-true-false

The tool generates true/false questions using deterministic transformation
and validation rules applied to the supplied input.

---

## 4. Difficulty Classification

The `classify-difficulty` tool uses an explicit deterministic scoring formula.

Score:

    (expected_answer_complexity * 1.5)
    + (number_of_concepts * 2.0)
    + (number_of_steps * 1.0)

Classification thresholds:

- Score < 10 → Easy
- Score < 20 → Medium
- Score >= 20 → Hard

The same input values always produce the same difficulty classification.

The classification is rule-based and is not produced by an LLM or machine
learning model.

---

## 5. Question-Set Validation

The `validate-question-set` tool checks the supplied question set against
explicit validation rules.

Validation includes:

- required question structure
- supported question types
- required fields
- answer consistency
- duplicate detection
- JSON/schema validity
- set-level consistency

Duplicate detection uses deterministic set-logic rather than probabilistic
similarity.

Validation results identify whether the supplied question set satisfies the
defined requirements.

---

## 6. Question-Set Analysis

The `analyze-question-set` tool analyzes a supplied question set using
deterministic calculations.

Analysis may include:

- question counts
- question-type distribution
- difficulty distribution
- structural characteristics
- validation-related observations

The analysis is derived only from the supplied question-set data.

---

## 7. Input → Decision → Output Traceability

For every tool invocation, the processing path is:

1. Receive the declared input.
2. Validate the input against the tool contract.
3. Apply the tool's documented deterministic rules.
4. Produce the corresponding structured output.
5. Validate the output where applicable.
6. Return the result.

Therefore, the resulting output can be traced to the input fields and the
documented rules of the invoked tool.

---

## 8. Determinism and Reproducibility

The agent is deterministic.

Given identical:

- inputs
- configuration
- tool version
- execution rules

the same processing path and result are expected.

The implementation does not rely on random number generation for core
question-generation or analysis behavior.

No hidden model inference is required for the core agent behavior.

---

## 9. External Knowledge and Dependencies

The agent does not retrieve external educational knowledge during question
generation.

Generated material is dependent on the information supplied to the agent.

Therefore:

- unsupported facts are not intentionally retrieved from the internet
- the agent does not claim external factual verification
- output quality depends on the supplied input
- external knowledge retrieval is outside the core agent behavior

---

## 10. Error and Validation Behavior

Invalid inputs are handled through explicit validation and tool contracts.

The agent should reject inputs that do not satisfy the required contract
instead of silently interpreting unsupported structures.

Validation failures are reported as structured errors or validation results,
depending on the tool contract.

This makes failures distinguishable from successful question generation.

---

## 11. Safety and Scope Boundaries

The agent is designed for educational question generation and question-set
analysis.

It does not:

- execute arbitrary user-provided code
- access undeclared external systems
- retrieve private information
- make decisions outside its declared educational scope
- silently modify external systems

The agent's behavior is limited to its declared tools and contracts.

---

## 12. Tool-Level Explainability Summary

| Tool | Primary Decision/Processing | Explainability Basis |
|------|-----------------------------|----------------------|
| generate-mcq | Generate MCQ structure | Deterministic templates and input |
| generate-short-answer | Generate short-answer structure | Deterministic templates and input |
| generate-long-answer | Generate long-answer structure | Deterministic templates and input |
| generate-true-false | Generate true/false structure | Deterministic transformation rules |
| classify-difficulty | Calculate difficulty class | Explicit scoring formula and thresholds |
| validate-question-set | Validate question set | Explicit schema and validation rules |
| analyze-question-set | Analyze question-set properties | Deterministic calculations |

---

## 13. Limitations

The agent does not independently establish the truth of arbitrary
educational content supplied by a user.

Because the core system is deterministic and does not use an LLM or external
knowledge source, it cannot independently compensate for missing or
incorrect source material.

Its outputs should therefore be interpreted as generated educational
scaffolding based on the supplied input and documented rules.

---

## 14. Auditability

The agent architecture separates:

- input contracts
- tool contracts
- deterministic processing logic
- validation
- output handling

This separation allows an evaluator or developer to inspect the relevant
tool implementation and determine how an output was produced.

The documentation in this file describes the decision rules and limitations
without requiring access to an opaque model reasoning process.

---

## 15. Non-LLM Nature

This agent uses no machine learning model for its core behavior.

Every core output is generated through deterministic program logic and
standard processing based on the supplied input.

There is no hidden chain-of-thought or undisclosed model inference involved
in the generation process.

---

## 16. Framework Independence

The agent core is independent of a specific agent framework.

Framework-specific translation is isolated behind adapter boundaries.

This means the same core behavior and tool contracts can be exposed through
compatible runtimes without changing the underlying educational logic.

---

## 17. Reproducibility Statement

For the same input and the same implementation/configuration, the agent is
designed to produce reproducible results.

Changes to:

- source input
- configuration
- tool implementation
- tool version

may change the resulting output.

Such changes should therefore be treated as versioned implementation changes
when reproducibility is required.
