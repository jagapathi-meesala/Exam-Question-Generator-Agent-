import os
import sys

def run_audit():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    required_files = [
        "agent.yaml", "README.md", "SOUL.md", "RULES.md", "DUTIES.md", "AGENTS.md", "EXPLAINABILITY.md",
        "requirements.txt", "pytest.ini", ".env.example", ".gitignore",
        "config/settings.py", "core/agent.py", "core/registry.py",
        "contracts/agent_contract.py", "contracts/tool_contract.py", "contracts/adapter.py",
        "adapters/registry.py", "adapters/portable_adapter.py",
        "tools/generate_mcq.py", "tools/generate_short_answer.py", "tools/generate_long_answer.py",
        "tools/generate_true_false.py", "tools/classify_difficulty.py", "tools/validate_question_set.py",
        "tools/analyze_question_set.py",
        "tools/generate-mcq.yaml", "tools/generate-short-answer.yaml", "tools/generate-long-answer.yaml",
        "tools/generate-true-false.yaml", "tools/classify-difficulty.yaml", "tools/validate-question-set.yaml",
        "tools/analyze-question-set.yaml",
        "tests/test_agent.py", "tests/test_registry.py", "tests/test_tools.py", "tests/test_security.py",
        "tests/test_documentation.py", "tests/test_adapters.py", "tests/test_open_gap_schema.py"
    ]
    
    missing = []
    for f in required_files:
        if not os.path.exists(os.path.join(base_dir, f)):
            missing.append(f)
            
    if missing:
        print("FAILED: Missing required files:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)
        
    print("PASSED")
    sys.exit(0)

if __name__ == "__main__":
    run_audit()
