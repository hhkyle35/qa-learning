# Guide: Adding Context to Your Projects

## Quick Start

There are three ways to add context to your projects:

### Option 1: Interactive Script (Easiest)

Run the interactive initialization script:

```bash
python3 scripts/init-context.py
```

This will guide you through adding context for each project with prompts.

### Option 2: Tell Claude (Recommended)

Just tell Claude what you want to add! For example:

- "I'm working on NourishRx. We just had a meeting about the MVP features. Add that to the context."
- "For the farm project, we're using Shopify and our top products are eggs, vegetables, and honey."
- "I'm learning SQL and I just finished a lesson on JOINs. Update my tech learning context."

Claude will automatically update the context files for you.

### Option 3: Manual Editing

Edit the JSON files directly in `context/<project-name>/context.json`

## What Context to Add

### For NourishRx (Startup Project)

**Essential Information:**
- Current focus: What you're working on right now
- Recent activity: What you've done recently
- Current tasks: Active work items
- Next steps: What's coming up
- Key decisions: Important decisions made
- Blockers: Things preventing progress
- Meeting notes: Important discussions
- Contacts: Key people involved

**Example:**
```json
{
  "currentFocus": "Building MVP features for beta testing",
  "recentActivity": [
    "Completed user authentication system",
    "Met with potential investors",
    "Designed onboarding flow"
  ],
  "currentTasks": [
    "Implement payment integration",
    "Write user documentation",
    "Prepare beta test plan"
  ],
  "nextSteps": [
    "Launch beta with 10 users",
    "Collect feedback",
    "Iterate on core features"
  ],
  "keyDecisions": [
    "Using Stripe for payments",
    "Focusing on web app first, mobile later"
  ]
}
```

### For Farm E-commerce & Marketing

**Essential Information:**
- E-commerce platform: Shopify, WooCommerce, etc.
- Products: Key products you're selling
- Marketing channels: Social media, email, etc.
- Active campaigns: Current marketing efforts
- Recent orders: Sales activity
- Current focus: What you're working on

**Example:**
```json
{
  "currentFocus": "Launching spring vegetable campaign",
  "ecommerce": {
    "platform": "Shopify",
    "products": ["Fresh Eggs", "Organic Vegetables", "Local Honey"],
    "recentOrders": ["Increased orders for spring vegetables"]
  },
  "marketing": {
    "activeCampaigns": ["Spring Vegetable Promotion", "Farmers Market Announcement"],
    "channels": ["Instagram", "Facebook", "Email Newsletter"]
  }
}
```

### For Accounting & Tax Learning

**Essential Information:**
- Current topic: What you're learning now
- Completed lessons: What you've finished
- Current lessons: What you're working on
- Key concepts: Important things you've learned
- Questions: Things you need to understand
- Resources: Courses, books, websites

**Example:**
```json
{
  "currentTopic": "Tax Deductions",
  "currentFocus": "Understanding business expense deductions",
  "completedLessons": [
    "Basic Accounting Principles",
    "Income Statements",
    "Balance Sheets"
  ],
  "currentLessons": [
    "Tax Deductions Overview",
    "Business Expense Categories"
  ],
  "keyConcepts": [
    "Ordinary and necessary business expenses",
    "Depreciation methods"
  ],
  "questions": [
    "What's the difference between Section 179 and bonus depreciation?",
    "Can I deduct home office expenses?"
  ]
}
```

### For Tech Skills Learning

**Essential Information:**
- Current skill: Which one you're focusing on (Selenium/Appium/SQL)
- Learning path status: Progress for each skill
- Current lessons: What you're learning
- Practice projects: Projects you're working on
- Code examples: Snippets you're learning
- Questions: Technical questions

**Example:**
```json
{
  "currentSkill": "sql",
  "currentFocus": "Learning complex JOINs and subqueries",
  "learningPaths": {
    "sql": {
      "status": "in_progress",
      "currentLesson": "Advanced JOINs",
      "completedLessons": [
        "Basic SELECT statements",
        "WHERE clauses",
        "Simple JOINs"
      ],
      "practiceProjects": [
        "Building a query for customer orders",
        "Analyzing sales data"
      ]
    }
  },
  "codeExamples": [
    "SELECT customers.name, orders.total FROM customers JOIN orders ON customers.id = orders.customer_id"
  ],
  "questions": [
    "When should I use LEFT JOIN vs INNER JOIN?",
    "How do I optimize slow queries?"
  ]
}
```

## Updating Context Over Time

### As You Work

Claude will automatically update context when you:
- Complete tasks
- Make decisions
- Add notes
- Switch focus

### Manual Updates

You can ask Claude to update context:
- "I just finished the payment integration for NourishRx, update the context"
- "Add 'completed SQL JOINs lesson' to my tech learning context"
- "I'm blocked on the farm's Shopify integration, add that to blockers"

### Regular Reviews

Periodically review and update:
- Completed tasks → move to `completedTasks`
- Update `nextSteps` as priorities change
- Archive old `recentActivity` items
- Update `currentFocus` as you switch work

## Tips

1. **Start Simple**: Just add the basics (current focus, next steps)
2. **Update Regularly**: Keep context current as you work
3. **Let Claude Help**: Claude can update context automatically
4. **Be Specific**: Detailed context helps Claude help you better
5. **Use Session History**: Check `session-history.md` to remember what you did

## Example Workflow

1. **Initialize**: Run the script or tell Claude to set up initial context
2. **Start Working**: Tell Claude which project you're on
3. **Work Normally**: Claude tracks and updates context
4. **Review**: Periodically check context files
5. **Update**: Add new information as needed

## Need Help?

Just ask Claude:
- "Help me add context for NourishRx"
- "What context should I add for the farm project?"
- "Update my SQL learning context with what I just learned"

Claude can guide you through adding any context you need!

