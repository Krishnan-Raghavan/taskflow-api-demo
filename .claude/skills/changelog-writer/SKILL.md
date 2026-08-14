---
name: changelog-writer
description: Automatically invoked after any code change to app/ — appends a one-line entry to CHANGELOG.md summarizing what changed and why.
---

# Changelog Writer

After modifying any file under `app/`, append a single new bullet line to
`CHANGELOG.md` (create it if it doesn't exist) summarizing the change in
plain English, in this format:

- YYYY-MM-DD: <short summary of the change>

Do not rewrite existing entries. Do not ask for confirmation — this runs
automatically as part of finishing the task.
