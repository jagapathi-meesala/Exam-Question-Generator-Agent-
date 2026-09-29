# Agent Architecture
- **Agent Core**: `AgentCore` serves as the integration layer managing the tool registry and metadata.
- **Tool Architecture**: Each tool is an isolated contract adhering to `ToolContract`. Tools expose deterministic `execute()` functions.
- **Extension Mechanism**: New tools are registered dynamically without modifying core dispatch logic.
- **Interoperability Strategy**: The `AgentAdapter` abstraction allows exporting the agent to external platforms (e.g., OpenGAP).
- **Framework Independence**: Zero dependencies on LangChain, AutoGen, or OpenAI SDK.
- **Portability Design**: Core logic is completely decoupled from HTTP handlers or specific runtime APIs.
