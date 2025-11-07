#!/usr/bin/env python3
"""
Context Loader Script
Loads and displays the current project context for Claude
"""

import json
import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
CONTEXT_DIR = BASE_DIR / "context"
ACTIVE_PROJECT_FILE = CONTEXT_DIR / "active-project.txt"

def get_active_project():
    """Get the currently active project"""
    if ACTIVE_PROJECT_FILE.exists():
        with open(ACTIVE_PROJECT_FILE, 'r') as f:
            project = f.read().strip()
            return project if project else None
    return None

def load_project_context(project_name):
    """Load context for a specific project"""
    context_file = CONTEXT_DIR / project_name / "context.json"
    if context_file.exists():
        with open(context_file, 'r') as f:
            return json.load(f)
    return None

def format_context_summary(context):
    """Format context as a readable summary"""
    if not context:
        return "No context available"
    
    summary = f"# {context.get('project', 'Unknown Project')}\n\n"
    summary += f"**Last Updated**: {context.get('lastUpdated', 'Unknown')}\n"
    summary += f"**Status**: {context.get('status', 'Unknown')}\n\n"
    
    if context.get('currentFocus'):
        summary += f"## Current Focus\n{context['currentFocus']}\n\n"
    
    if context.get('currentTasks'):
        summary += "## Current Tasks\n"
        for task in context['currentTasks']:
            summary += f"- {task}\n"
        summary += "\n"
    
    if context.get('nextSteps'):
        summary += "## Next Steps\n"
        for step in context['nextSteps']:
            summary += f"- {step}\n"
        summary += "\n"
    
    if context.get('importantNotes'):
        summary += "## Important Notes\n"
        for note in context['importantNotes']:
            summary += f"- {note}\n"
        summary += "\n"
    
    if context.get('blockers'):
        summary += "## Blockers\n"
        for blocker in context['blockers']:
            summary += f"- {blocker}\n"
        summary += "\n"
    
    return summary

def main():
    active_project = get_active_project()
    
    if not active_project or active_project == "none":
        print("No active project set. Available projects:")
        for project_dir in CONTEXT_DIR.iterdir():
            if project_dir.is_dir() and (project_dir / "context.json").exists():
                print(f"  - {project_dir.name}")
        return
    
    context = load_project_context(active_project)
    if context:
        print(format_context_summary(context))
    else:
        print(f"Context not found for project: {active_project}")

if __name__ == "__main__":
    main()

