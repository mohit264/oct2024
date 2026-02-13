# GitHub Copilot Chat Configuration

This repository includes VSCode configuration to enable GitHub Copilot Chat features.

## Features Enabled

The `.vscode/settings.json` file enables the following GitHub Copilot Chat features:

### 1. Agent Mode (`@workspace`, `@vscode`, `@terminal`)
- **Setting**: `github.copilot.chat.experimental.agentEnabled: true`
- **Description**: Enables specialized agents that can help with different aspects of your project
  - `@workspace` - Ask questions about your entire workspace/codebase
  - `@vscode` - Get help with VSCode commands and features
  - `@terminal` - Get assistance with terminal commands

### 2. Planning Mode
- **Setting**: `github.copilot.chat.planning.enabled: true`
- **Description**: Enables the `/plan` command in chat to help create step-by-step plans for implementing features or solving problems

### 3. Chat Edits
- **Setting**: `github.copilot.chat.edits.enabled: true`
- **Description**: Allows Copilot to suggest and make direct edits to your code through the chat interface

### 4. Terminal Context
- **Setting**: `github.copilot.chat.terminalContext.enabled: true`
- **Description**: Enables Copilot to understand terminal output and provide context-aware assistance

### 5. Editor Auto-completions
- **Setting**: `github.copilot.editor.enableAutoCompletions: true`
- **Description**: Enables inline code suggestions while you type

## How to Use

After opening this repository in VSCode:

1. **Reload VSCode** - Close and reopen VSCode or use `Ctrl+Shift+P` → "Developer: Reload Window"
2. **Open Chat** - Press `Ctrl+Alt+I` (Windows/Linux) or `Cmd+Alt+I` (Mac) to open GitHub Copilot Chat
3. **Use Agents** - Type `@` in the chat to see available agents:
   - `@workspace` - For codebase questions
   - `@vscode` - For VSCode help
   - `@terminal` - For terminal assistance
4. **Use Planning** - Type `/plan` followed by your request to get a structured plan
5. **Ask Questions** - Simply type your question in natural language

## Requirements

- **GitHub Copilot Subscription** - Active GitHub Copilot license
- **VSCode Version** - VS Code 1.85 or later recommended (released November 2023 or newer)
  - Some experimental features may require the latest stable version
  - To check your version: Help → About
- **Extensions**:
  - GitHub Copilot (required)
  - GitHub Copilot Chat (required)

**Note**: The settings in this repository use experimental features that may change in future versions. Always refer to the [official GitHub Copilot documentation](https://docs.github.com/en/copilot) for the most up-to-date information.

## Troubleshooting

If you don't see the agent/plan/ask options:

1. **Verify Extension Installation**:
   - Open Extensions panel (`Ctrl+Shift+X`)
   - Search for "GitHub Copilot" and "GitHub Copilot Chat"
   - Install both extensions if not already installed

2. **Check Copilot Status**:
   - Click on the Copilot icon in the bottom status bar
   - Ensure you're signed in and have an active subscription

3. **Reload Window**:
   - Press `Ctrl+Shift+P` → "Developer: Reload Window"

4. **Update VSCode**:
   - Check for updates: Help → Check for Updates
   - Some features require recent VSCode versions

5. **Check Settings**:
   - Verify `.vscode/settings.json` is present in the repository
   - Settings should be automatically loaded when you open the project

## Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VSCode Copilot Chat Guide](https://code.visualstudio.com/docs/copilot/copilot-chat)
