# Claude Skills Guide for Knowledge Base

## Creating Skills for Your Projects

### Skill Structure

Each Skill should be focused on a specific project or task. Here are examples for your projects:

## 1. NourishRx Project Skill

**Skill Name**: `nourishrx-assistant`

**Purpose**: Help with NourishRx startup tasks and documentation

**Capabilities**:
- Generate project updates
- Structure meeting notes
- Create task lists
- Draft client communications
- Generate documentation from conversations

**Example Use Cases**:
- "Create a project update for NourishRx based on this week's progress"
- "Structure these meeting notes into the knowledge base format"
- "Generate a client communication email"

## 2. Farm E-commerce Skill

**Skill Name**: `farm-marketing-assistant`

**Purpose**: Assist with farm e-commerce and marketing tasks

**Capabilities**:
- Generate product descriptions
- Create social media content
- Draft email campaigns
- Analyze sales data
- Generate marketing reports

**Example Use Cases**:
- "Create a product description for [product name]"
- "Generate this week's social media content calendar"
- "Summarize sales data from last month"

## 3. Accounting Learning Skill

**Skill Name**: `accounting-tutor`

**Purpose**: Assist with accounting and tax learning

**Capabilities**:
- Explain accounting concepts
- Help with practice problems
- Organize study notes
- Recommend learning resources
- Create study guides

**Example Use Cases**:
- "Explain double-entry bookkeeping"
- "Help me solve this accounting problem"
- "Create a study guide for tax preparation"

## 4. Tech Skills Learning Skill

**Skill Name**: `tech-mentor`

**Purpose**: Assist with technical learning (Selenium, Appium, SQL)

**Capabilities**:
- Code review and suggestions
- Debugging assistance
- Explain technical concepts
- Create practice exercises
- Generate code examples

**Example Use Cases**:
- "Review this Selenium test and suggest improvements"
- "Help me debug this SQL query"
- "Create a practice exercise for Appium"

## 5. Knowledge Base Management Skill

**Skill Name**: `kb-manager`

**Purpose**: Help manage and organize the knowledge base itself

**Capabilities**:
- Add new pages/sections
- Update existing content
- Organize information
- Create templates
- Generate summaries

**Example Use Cases**:
- "Add a new page for [topic] to the knowledge base"
- "Update the NourishRx project section with this information"
- "Create a template for meeting notes"

## How to Use Skills with Claude Code

1. **Create Skills**: Define Skills in Claude's interface or via API
2. **Invoke Skills**: Ask Claude to use a specific Skill
3. **Combine Skills**: Use multiple Skills together for complex tasks
4. **Update Skills**: Refine Skills based on usage

## Integration with MCP

Skills can work with MCP servers to:
- Access external data sources
- Update files automatically
- Query databases
- Integrate with APIs
- Perform complex workflows

## Example Workflow

```
User: "Add today's NourishRx meeting notes to the knowledge base"

Claude:
1. Uses "nourishrx-assistant" Skill to structure notes
2. Uses MCP filesystem server to read current notes.md
3. Uses MCP filesystem server to append structured notes
4. Uses "kb-manager" Skill to format for MkDocs
5. Updates the knowledge base file
```

## Best Practices

1. **Keep Skills Focused**: One Skill per major task/project
2. **Use Descriptive Names**: Make it clear what each Skill does
3. **Document Capabilities**: Note what each Skill can and cannot do
4. **Iterate**: Refine Skills based on actual usage
5. **Combine**: Use Skills together for complex workflows

