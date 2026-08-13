# Demo Use Case: TaskFlow API — Fixing a Real Client Bug with Claude Code

## The scenario (show this slide before opening the terminal)

You've just joined a client engagement. The client's team has handed you a
small existing codebase — a Python task-management API — and a bug ticket.
You've never seen this code before. Normally this means:

- Reading through unfamiliar files to understand structure and conventions
- Locating the relevant code for the bug
- Writing the fix
- Writing or updating tests
- Making sure nothing else broke
- Writing a clear commit message and PR description for review

That's typically **hours** of ramp-up and careful work for a new team member.
Today, we'll do it live, start to finish, with Claude Code.

---

## The ticket (this is what Claude Code will actually receive)

> **Bug:** `POST /tasks` accepts empty or missing task titles.
>
> **Expected behavior:** Creating a task with an empty or missing `title`
> should return `400 Bad Request` with a clear error message, instead of
> silently creating a blank task.
>
> **Acceptance criteria:**
> - Empty string title → `400`
> - Missing title field entirely → `400`
> - Valid title → `201`, unchanged from current behavior
> - Existing test suite continues to pass
> - No changes to unrelated endpoints

---

## What the audience will watch happen, in order

1. **Onboarding** — Claude Code reads the unfamiliar codebase and generates
   its own project notes (`CLAUDE.md`), the way a new hire would take notes
   on day one — except in seconds, not hours.
2. **Understanding** — asked where the bug likely lives, Claude Code points
   to the actual file and function, grounded in the real code, not a guess.
3. **A small custom automation, built live** — a lightweight rule ("skill")
   that automatically keeps a changelog updated whenever the code changes,
   showing how easy it is to extend Claude Code to a team's own conventions.
4. **The fix** — Claude Code implements the validation, referencing the
   ticket above, and runs the existing tests itself to confirm nothing else
   broke.
5. **A quality gate, enforced automatically** — a rule ("hook") that
   physically will not let Claude Code call the task finished until the
   test suite passes. This isn't a prompt asking politely — it's an
   enforced check outside the model's control.
6. **Ready for review** — Claude Code drafts the commit message and PR
   description directly from the change, ready to hand to a human reviewer.

## The takeaway line

*"From an unfamiliar codebase and a bug ticket, to a tested, reviewed,
PR-ready fix — in one sitting. That's the daily reality for every developer
on every one of our client engagements, and it's exactly what this course
teaches your team to set up and rely on."*
