# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is
A tiny Flask REST API for managing tasks, backed by an in-memory store (no database). Built as a small, self-contained **Claude Code demo repo** (see `TICKET.md` for the demo script/narrative) — code changes here should stay minimal and dependency-free in that spirit.

## Commands
```bash
# Setup (from taskflow-api/)
python -m venv .venv
.venv\Scripts\activate       # Windows; source .venv/bin/activate on macOS/Linux
pip install -r requirements.txt

# Run the app (http://127.0.0.1:5000)
python -m app.main

# Run the full test suite
pytest -v

# Run a single test
pytest tests/test_tasks.py::test_create_task_rejects_empty_title -v
```
All commands run from the `taskflow-api/` directory (this file's directory), not the repo checkout root above it.

A `Stop` hook in `.claude/settings.json` runs `pytest -q` automatically whenever Claude Code finishes a turn in this project, and blocks completion if any test fails — treat a failing suite as blocking, not advisory.

## Architecture
- `app/main.py` — Flask app factory (`create_app`), registers the `tasks` blueprint. Running the module directly starts the dev server.
- `app/routes.py` — all HTTP routes, under blueprint `bp` (no URL prefix).
- `app/models.py` — `Task` dataclass and `TaskStore`, an in-memory dict-backed repository keyed by an auto-incrementing id. `store` is a module-level singleton imported and used directly by routes (no dependency injection).
- `tests/conftest.py` — `client` fixture; clears `store._tasks` before each test to prevent state leaking between tests (the store is process-wide, not per-request).
- `tests/test_tasks.py` — route-level tests using Flask's test client.

## Endpoints
- `POST /tasks` — create (`{"title": "..."}`) → 201, or 400 if `title` is missing/empty/whitespace-only
- `GET /tasks` — list → 200
- `GET /tasks/<id>` — fetch one → 200 / 404
- `PATCH /tasks/<id>` — update `title` and/or `done` → 200 / 404
- `DELETE /tasks/<id>` — delete → 204 / 404

## Conventions
- Routes return `jsonify(vars(task))` — relies on `Task` staying a plain dataclass with no non-serializable fields.
- Not-found responses use `{"error": "..."}` with 404; the same shape is used for the 400 validation error on `POST /tasks`.
- `request.get_json(silent=True) or {}` is the pattern for tolerating missing/invalid JSON bodies — follow it for any new route rather than calling `request.get_json()` directly.
- No auth, no persistence — everything resets when the process restarts (and explicitly in tests via the `client` fixture).
- When a code change touches `app/`, use the `changelog` skill (`.claude/skills/changelog/`) to add a one-line, user-facing entry to `CHANGELOG.md` under `## Unreleased`.
