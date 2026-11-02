---
name: get-started
description: Connect Docu-Coach and read a person's timeline, open follow-ups, or this month's record counts.
---

# Get started with Docu-Coach

Docu-Coach is read-only. Connect `https://www.docu-coach.com/mcp`, sign in, and approve the consent screen.

Use the tools for the signed-in member's own organization:

1. Call `list_employees` when you need a person's id.
2. Call `get_employee_timeline` with that id.
3. Call `get_follow_ups` for open to-dos and checklist steps.
4. Call `search_records` for a short excerpt match.
5. Call `get_insights` for this month's counts.

Do not invent a record that a tool did not return. Empty results mean nothing visible matched.
