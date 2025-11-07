# Knowledge Base

A personal knowledge base built with MkDocs for managing multiple projects and learning resources.

## Projects Included

- **NourishRx**: Startup project documentation
- **Farm E-commerce & Marketing**: Managing local farm operations
- **Accounting & Tax**: Learning resources and notes
- **Tech Skills**: Selenium, Appium, SQL, and other upskilling resources

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Serve locally:
```bash
mkdocs serve
```

3. Open in browser:
```
http://127.0.0.1:8000
```

## Building for Deployment

Build static site:
```bash
mkdocs build
```

The site will be built in the `site/` directory.

## Deployment Options

### GitHub Pages
1. Install `mkdocs gh-deploy` plugin: `pip install mkdocs-git-revision-date-localized-plugin`
2. Deploy: `mkdocs gh-deploy`

### Netlify
1. Connect your repository to Netlify
2. Build command: `mkdocs build`
3. Publish directory: `site`

### Vercel
1. Connect your repository to Vercel
2. Build command: `mkdocs build`
3. Output directory: `site`

## Project Context System

This knowledge base includes a **Project Context System** that allows Claude to:
- **Remember where you left off** in each project
- **Switch between projects** seamlessly
- **Maintain project-specific context** automatically
- **Track session history** for each project

### Quick Start

1. **Switch to a project**:
   ```bash
   ./scripts/switch-project.sh nourishrx
   ```
   Or just tell Claude: "I'm working on NourishRx now"

2. **View current context**:
   ```bash
   python3 scripts/load-context.py
   ```

3. **Work on your project** - Claude will automatically:
   - Load the project's context
   - Remember recent activity
   - Update context as you work
   - Help you pick up where you left off

See [Project Context System](docs/project-context-system.md) for full documentation.

## Using with Claude Code

Claude Code can help you:
- Write and edit markdown files
- Add new sections and pages
- Improve navigation structure
- Add features and plugins
- Maintain and update content
- **Load and update project context automatically**
- **Switch between projects seamlessly**

Just tell Claude which project you're working on, and it will understand the context!

## Structure

```
docs/
├── index.md                    # Homepage
├── projects/                   # Project documentation
│   ├── nourishrx/
│   └── farm/
├── learning/                   # Learning resources
│   ├── accounting/
│   └── tech/
└── templates.md               # Documentation templates

context/                        # Project context system
├── active-project.txt         # Current project indicator
├── nourishrx/
│   ├── context.json          # Project state
│   └── session-history.md    # Activity log
├── farm/
├── accounting/
└── tech-learning/

scripts/
├── switch-project.sh          # Switch active project
└── load-context.py            # View current context
```

## Features

- 🔍 Full-text search across all content
- 📱 Responsive design (works on mobile)
- 🌓 Dark mode support
- 🔗 Automatic navigation and linking
- 📝 Markdown-based (easy to edit)
- 🔄 Version controlled with Git
- 🧠 **Project context system** - Claude remembers where you left off
- 🔄 **Seamless project switching** - Switch between projects easily
- 📊 **Session history tracking** - Never lose your place

