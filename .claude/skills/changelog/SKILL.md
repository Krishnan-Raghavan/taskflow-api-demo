---
name: changelog
description: Keep CHANGELOG.md up to date whenever code in app/ changes. Use this after making or finishing any code change to app/ files (bug fixes, new endpoints, behavior changes) — not for docs-only or test-only edits.
---

# Changelog skill

When a change to `app/` is complete (bug fix, new endpoint, behavior change):

1. Open `CHANGELOG.md` at the repo root. Create it if missing, with an `# Changelog` heading and an `## Unreleased` section.
2. Add one bullet under `## Unreleased` describing the change from a user/API-consumer perspective (what behavior changed, not implementation detail). Example: `- POST /tasks now returns 400 for empty or missing title instead of silently creating a blank task.`
3. Don't touch entries for unrelated changes. Don't invent a version number or date — that happens at release time, not here.
4. Keep each entry to one line.
