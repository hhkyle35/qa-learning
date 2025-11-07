#!/bin/bash
# Switch active project context

PROJECT_NAME=$1
CONTEXT_DIR="$(dirname "$0")/../context"
ACTIVE_PROJECT_FILE="$CONTEXT_DIR/active-project.txt"

if [ -z "$PROJECT_NAME" ]; then
    echo "Usage: ./switch-project.sh <project-name>"
    echo ""
    echo "Available projects:"
    for dir in "$CONTEXT_DIR"/*; do
        if [ -d "$dir" ] && [ -f "$dir/context.json" ]; then
            echo "  - $(basename "$dir")"
        fi
    done
    exit 1
fi

if [ ! -f "$CONTEXT_DIR/$PROJECT_NAME/context.json" ]; then
    echo "Error: Project '$PROJECT_NAME' not found"
    exit 1
fi

echo "$PROJECT_NAME" > "$ACTIVE_PROJECT_FILE"
echo "Switched to project: $PROJECT_NAME"
echo ""
echo "Context loaded. Claude will now understand you're working on: $PROJECT_NAME"

