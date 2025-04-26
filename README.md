# Resolvr

> Turn messy goals into structured, actionable plans.

---

## 📖 Core Idea Behind *Resolvr*

Resolvr is a personal productivity tool built to bridge the gap between **brain-dump chaos** and **focused action**.

You create simple Markdown files (daily or weekly) where you freely list your tasks, ideas, and goals — messy, unfiltered, natural.

Then **Resolvr** (your script + ChatGPT) processes that raw material into:
1. Prioritized goals (what really matters now)
2. Structured micro-actions (small first steps to destroy procrastination inertia)
3. Full detailed action plans (organized, clean, and motivating)

It’s not just about organizing.  
It’s about **breaking the mental barriers** that block real action — especially built with ADHD minds in mind.

---

## 🧠 How Resolvr Works (Concept Overview)

- **Step 1**: You write a journal entry (`new_journal.py`) — today's goals, ideas, thoughts.
- **Step 2**: You run **Resolvr** (`resolvr.py`) to extract and format your goals into a ready-to-use prompt.
- **Step 3**: You paste the prompt into a dedicated ChatGPT project.
- **Step 4**: ChatGPT dynamically helps:
  - Clarify confusing goals
  - Build small first steps
  - Organize structured plans
  - Add realistic time estimates
  - Export a clean Markdown action file (`*_task_ready.md`)
- **Step 5**: You move the final plan into your `tasks-ready/` folder for execution and organization.

#### Notes
*You can edit the existing prompt that chatGPT will use. It's under the `templates/` directory*

---

## 🚀 Setup Instructions

You'll need:
- Python 3.8+
- ChatGPT
- Basic terminal familiarity
- A Markdown editor (or just Neovim/VSCode)

