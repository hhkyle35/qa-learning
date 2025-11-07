# Project Context System

## Overview

The Project Context System allows you to maintain separate context for each project, enabling Claude to understand where you left off and maintain project-specific knowledge when you switch between projects.

## How It Works

### 1. Context Storage

Each project has its own context stored in `context/<project-name>/context.json`:
- Current status and focus
- Recent activity
- Current and completed tasks
- Blockers and next steps
- Important notes
- Related files

### 2. Active Project Indicator

The `context/active-project.txt` file indicates which project you're currently working on. Claude reads this file to understand which context to load.

### 3. Session History

Each project has a `session-history.md` file that tracks your work sessions, helping you pick up where you left off.

## Usage

### Switching Projects

**Option 1: Manual**
```bash
echo "nourishrx" > context/active-project.txt
```

**Option 2: Using Script**
```bash
./scripts/switch-project.sh nourishrx
```

**Option 3: Tell Claude**
Just say: "I'm switching to work on the NourishRx project" and Claude will update the active project file.

### Viewing Current Context

```bash
python3 scripts/load-context.py
```

Or ask Claude: "What's the current context for my active project?"

### Updating Context

Claude automatically updates context as you work:
- When you complete a task
- When you make a decision
- When you encounter a blocker
- When you add notes

You can also manually update context files, or ask Claude to update them.

## Project Names

- `nourishrx` - NourishRx startup project
- `farm` - Farm e-commerce & marketing
- `accounting` - Accounting & tax learning
- `tech-learning` - Tech skills learning (Selenium, Appium, SQL)

## Context File Structure

Each `context.json` includes:

```json
{
  "project": "Project Name",
  "lastUpdated": "ISO timestamp",
  "status": "active|paused|completed",
  "currentFocus": "What you're currently working on",
  "recentActivity": ["List of recent actions"],
  "currentTasks": ["Active tasks"],
  "completedTasks": ["Recently completed"],
  "blockers": ["Things blocking progress"],
  "keyDecisions": ["Important decisions made"],
  "nextSteps": ["What to do next"],
  "importantNotes": ["Key information"],
  "relatedFiles": ["Paths to related documentation"]
}
```

## Integration with Claude

### Automatic Context Loading

When you start a conversation, Claude will:
1. Check `context/active-project.txt`
2. Load the corresponding `context.json`
3. Read recent `session-history.md`
4. Understand your current project state

### Context-Aware Responses

Claude will:
- Remember where you left off
- Reference recent decisions and notes
- Suggest next steps based on context
- Update context as you work

### Example Workflow

1. **Switch Project**: "I'm working on NourishRx now"
   - Claude updates `active-project.txt`
   - Loads NourishRx context

2. **Work on Project**: "Add the meeting notes from today"
   - Claude understands NourishRx context
   - Adds notes to appropriate files
   - Updates context with recent activity

3. **Switch Again**: "Let me work on SQL learning"
   - Claude switches to tech-learning context
   - Remembers where you were in SQL learning
   - Continues from that point

## Benefits

✅ **Context Switching**: Seamlessly switch between projects  
✅ **Continuity**: Pick up exactly where you left off  
✅ **Organization**: Each project maintains its own state  
✅ **Claude Awareness**: Claude understands which project you're working on  
✅ **History Tracking**: Session history helps remember what you did  
✅ **Related Files**: Quick access to project documentation  

## MCP Integration

The context system works with MCP servers:
- Filesystem MCP can read/write context files
- Claude can automatically update context via MCP
- Context can be queried programmatically

## Best Practices

1. **Update Active Project**: Always set active project when switching
2. **Let Claude Update**: Allow Claude to automatically update context
3. **Review Context**: Periodically review context files for accuracy
4. **Session History**: Check session history to remember past work
5. **Related Files**: Keep related files list updated

