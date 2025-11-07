# Project Context System

This directory stores structured context for each project, allowing Claude to understand where you left off and maintain project-specific knowledge.

## How It Works

1. **Context Files**: Each project has a `context.json` file with current state
2. **Active Project**: The `active-project.txt` file indicates which project you're currently working on
3. **MCP Integration**: Claude can read context files via MCP to understand project state
4. **Auto-updates**: Context files are updated as you work

## Structure

```
context/
├── active-project.txt          # Current project indicator
├── nourishrx/
│   ├── context.json            # Project state and context
│   └── session-history.md      # Recent activity log
├── farm/
│   ├── context.json
│   └── session-history.md
├── accounting/
│   ├── context.json
│   └── session-history.md
└── tech-learning/
    ├── context.json
    └── session-history.md
```

## Usage

When you start working on a project:
1. Update `active-project.txt` with the project name
2. Claude will automatically load that project's context
3. As you work, context is updated automatically
4. When you switch projects, just update `active-project.txt`

## Context File Structure

Each `context.json` contains:
- Current focus/status
- Recent tasks completed
- Current blockers
- Key decisions made
- Next steps
- Important notes
- Related files/documents

