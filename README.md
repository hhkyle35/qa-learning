# Knowledge Base

A personal knowledge base built with MkDocs for managing multiple projects and learning resources.

**Live Site**: https://hhkyle35.github.io/qa-learning/

## Projects Included

- **NourishRx**: Startup project documentation
- **Farm E-commerce & Marketing**: Managing local farm operations
- **Accounting & Tax**: Learning resources and notes
- **Tech Skills**: Selenium, Appium, SQL, and other upskilling resources

## Setup

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Serve locally:
```bash
mkdocs serve
```

4. Open in browser:
```
http://127.0.0.1:8000
```

## Building for Deployment

Build static site:
```bash
mkdocs build
```

The site will be built in the `site/` directory.

## Deployment

### Automatic Deployment (Recommended)

This repository is configured with **GitHub Actions** for automatic deployment:

- **Every push to `main`** automatically deploys to GitHub Pages
- **No manual steps required** - just commit and push your changes
- **View your site at**: https://hhkyle35.github.io/qa-learning/

### Manual Deployment

To deploy manually from your local machine:

```bash
source venv/bin/activate
mkdocs gh-deploy
```

This builds the site and pushes it to the `gh-pages` branch.

## Making Updates

1. **Edit markdown files** in the `docs/` directory
2. **Preview locally** with `mkdocs serve`
3. **Commit and push** to deploy:
   ```bash
   git add .
   git commit -m "Update documentation"
   git push
   ```
4. **Wait ~1 minute** for GitHub Actions to deploy
5. **View changes** at https://hhkyle35.github.io/qa-learning/

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

