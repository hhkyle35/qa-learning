#!/usr/bin/env python3
"""
Interactive Context Initialization Script
Helps you populate context files for each project
"""

import json
import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
CONTEXT_DIR = BASE_DIR / "context"

PROJECTS = {
    "nourishrx": {
        "name": "NourishRx",
        "description": "Startup project"
    },
    "farm": {
        "name": "Farm E-commerce & Marketing",
        "description": "Managing e-commerce and marketing for a local farm"
    },
    "accounting": {
        "name": "Accounting & Tax Learning",
        "description": "Learning accounting and tax preparation"
    },
    "tech-learning": {
        "name": "Tech Skills Learning",
        "description": "Learning Selenium, Appium, SQL, and other tech skills"
    }
}

def get_input(prompt, default=""):
    """Get user input with optional default"""
    if default:
        response = input(f"{prompt} [{default}]: ").strip()
        return response if response else default
    return input(f"{prompt}: ").strip()

def get_list_input(prompt):
    """Get a list of items from user"""
    print(f"\n{prompt}")
    print("(Enter one item per line, empty line to finish)")
    items = []
    while True:
        item = input("  - ").strip()
        if not item:
            break
        items.append(item)
    return items

def init_nourishrx():
    """Initialize NourishRx context"""
    print("\n" + "="*60)
    print("Initializing NourishRx Project Context")
    print("="*60)
    
    context = {
        "project": "NourishRx",
        "lastUpdated": datetime.now().isoformat(),
        "status": get_input("Status", "active"),
        "currentFocus": get_input("What are you currently focused on?"),
        "recentActivity": get_list_input("Recent activity (what have you done recently?)"),
        "currentTasks": get_list_input("Current tasks (what are you working on now?)"),
        "completedTasks": get_list_input("Recently completed tasks"),
        "blockers": get_list_input("Any blockers or issues?"),
        "keyDecisions": get_list_input("Key decisions made recently"),
        "nextSteps": get_list_input("What are your next steps?"),
        "importantNotes": get_list_input("Important notes or information"),
        "relatedFiles": [
            "../docs/projects/nourishrx/index.md",
            "../docs/projects/nourishrx/notes.md",
            "../docs/projects/nourishrx/tasks.md"
        ],
        "meetingNotes": get_list_input("Recent meeting notes or topics"),
        "contacts": get_list_input("Key contacts (name: role)"),
        "resources": get_list_input("Important resources or links")
    }
    
    return context

def init_farm():
    """Initialize Farm context"""
    print("\n" + "="*60)
    print("Initializing Farm E-commerce & Marketing Context")
    print("="*60)
    
    context = {
        "project": "Farm E-commerce & Marketing",
        "lastUpdated": datetime.now().isoformat(),
        "status": get_input("Status", "active"),
        "currentFocus": get_input("What are you currently focused on?"),
        "recentActivity": get_list_input("Recent activity"),
        "currentTasks": get_list_input("Current tasks"),
        "completedTasks": get_list_input("Recently completed tasks"),
        "blockers": get_list_input("Any blockers?"),
        "keyDecisions": get_list_input("Key decisions"),
        "nextSteps": get_list_input("Next steps"),
        "importantNotes": get_list_input("Important notes"),
        "relatedFiles": [
            "../docs/projects/farm/index.md",
            "../docs/projects/farm/ecommerce.md",
            "../docs/projects/farm/marketing.md",
            "../docs/projects/farm/notes.md"
        ],
        "ecommerce": {
            "platform": get_input("E-commerce platform (e.g., Shopify, WooCommerce)", ""),
            "products": get_list_input("Key products"),
            "recentOrders": get_list_input("Recent orders or sales notes")
        },
        "marketing": {
            "activeCampaigns": get_list_input("Active marketing campaigns"),
            "channels": get_list_input("Marketing channels (social media, email, etc.)")
        }
    }
    
    return context

def init_accounting():
    """Initialize Accounting learning context"""
    print("\n" + "="*60)
    print("Initializing Accounting & Tax Learning Context")
    print("="*60)
    
    context = {
        "project": "Accounting & Tax Learning",
        "lastUpdated": datetime.now().isoformat(),
        "status": get_input("Status", "active"),
        "currentFocus": get_input("What are you currently learning?"),
        "currentTopic": get_input("Current topic or chapter"),
        "recentActivity": get_list_input("Recent learning activity"),
        "completedLessons": get_list_input("Completed lessons or chapters"),
        "currentLessons": get_list_input("Lessons you're currently working on"),
        "practiceProblems": get_list_input("Practice problems you're working on"),
        "questions": get_list_input("Questions you have"),
        "keyConcepts": get_list_input("Key concepts you've learned"),
        "nextSteps": get_list_input("Next learning steps"),
        "importantNotes": get_list_input("Important notes"),
        "relatedFiles": [
            "../docs/learning/accounting/index.md",
            "../docs/learning/accounting/concepts.md",
            "../docs/learning/accounting/resources.md",
            "../docs/learning/accounting/notes.md"
        ],
        "resources": {
            "courses": get_list_input("Courses you're taking"),
            "books": get_list_input("Books you're reading"),
            "websites": get_list_input("Useful websites")
        }
    }
    
    return context

def init_tech_learning():
    """Initialize Tech learning context"""
    print("\n" + "="*60)
    print("Initializing Tech Skills Learning Context")
    print("="*60)
    
    skills = {}
    for skill in ["selenium", "appium", "sql"]:
        print(f"\n--- {skill.upper()} ---")
        skills[skill] = {
            "status": get_input(f"{skill.capitalize()} status", "not_started"),
            "currentLesson": get_input(f"Current {skill} lesson"),
            "completedLessons": get_list_input(f"Completed {skill} lessons"),
            "practiceProjects": get_list_input(f"{skill.capitalize()} practice projects")
        }
    
    context = {
        "project": "Tech Skills Learning",
        "lastUpdated": datetime.now().isoformat(),
        "status": get_input("Overall status", "active"),
        "currentFocus": get_input("What are you currently learning?"),
        "currentSkill": get_input("Which skill are you focusing on? (selenium/appium/sql)"),
        "recentActivity": get_list_input("Recent learning activity"),
        "learningPaths": skills,
        "currentTasks": get_list_input("Current learning tasks"),
        "completedTasks": get_list_input("Completed tasks"),
        "codeExamples": get_list_input("Code examples or snippets you're working on"),
        "questions": get_list_input("Questions you have"),
        "nextSteps": get_list_input("Next learning steps"),
        "importantNotes": get_list_input("Important notes"),
        "relatedFiles": [
            "../docs/learning/tech/index.md",
            "../docs/learning/tech/selenium.md",
            "../docs/learning/tech/appium.md",
            "../docs/learning/tech/sql.md",
            "../docs/learning/tech/notes.md"
        ],
        "resources": {
            "courses": get_list_input("Courses you're taking"),
            "practicePlatforms": get_list_input("Practice platforms (LeetCode, HackerRank, etc.)"),
            "documentation": get_list_input("Documentation you're using")
        }
    }
    
    return context

def save_context(project_name, context):
    """Save context to file"""
    context_file = CONTEXT_DIR / project_name / "context.json"
    with open(context_file, 'w') as f:
        json.dump(context, f, indent=2)
    print(f"\n✅ Context saved to {context_file}")

def main():
    print("Project Context Initialization")
    print("="*60)
    print("\nAvailable projects:")
    for key, info in PROJECTS.items():
        print(f"  {key}: {info['name']} - {info['description']}")
    
    print("\nOptions:")
    print("  1. Initialize all projects")
    print("  2. Initialize specific project")
    print("  3. Exit")
    
    choice = input("\nChoice [1-3]: ").strip()
    
    if choice == "1":
        for project_name in PROJECTS.keys():
            if project_name == "nourishrx":
                context = init_nourishrx()
            elif project_name == "farm":
                context = init_farm()
            elif project_name == "accounting":
                context = init_accounting()
            elif project_name == "tech-learning":
                context = init_tech_learning()
            else:
                continue
            
            save_context(project_name, context)
            print()
    
    elif choice == "2":
        print("\nWhich project?")
        for key in PROJECTS.keys():
            print(f"  - {key}")
        project = input("Project name: ").strip()
        
        if project not in PROJECTS:
            print(f"❌ Unknown project: {project}")
            return
        
        if project == "nourishrx":
            context = init_nourishrx()
        elif project == "farm":
            context = init_farm()
        elif project == "accounting":
            context = init_accounting()
        elif project == "tech-learning":
            context = init_tech_learning()
        
        save_context(project, context)
    
    elif choice == "3":
        print("Exiting...")
        return
    else:
        print("Invalid choice")
        return
    
    print("\n✨ Context initialization complete!")
    print("\nNext steps:")
    print("  1. Review the context files in context/")
    print("  2. Switch to a project: ./scripts/switch-project.sh <project>")
    print("  3. Start working - Claude will use this context automatically")

if __name__ == "__main__":
    main()

