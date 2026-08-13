# TaskFlow API — Project Notes

## What this is
A tiny Flask REST API for managing tasks, backed by an in-memory store (no database). Built as a small, self-contained demo repo.

## Structure
- `app/main.py` — Flask app factory (`create_app`), registers the `tasks` blueprint.
- `app/routes.py` — all HTTP routes, under blueprint `bp` (no URL prefix).
- `app/models.py` — `Task` dataclass and `TaskStore`, an in-memory dict-backed repository. `store` is a module-level singleton used directly by routes.
- `tests/conftest.py` — `client` fixture; clears `store._tasks` before each test to prevent state leaking between tests.
- `tests/test_tasks.py` — route-level tests using Flask's test client.

## Endpoints
- `POST /tasks` — create (`{"title": "..."}`) → 201
- `GET /tasks` — list → 200
- `GET /tasks/<id>` — fetch one → 200 / 404
- `PATCH /tasks/<id>` — update `title` and/or `done` → 200 / 404
- `DELETE /tasks/<id>` — delete → 204 / 404

## Conventions
- Routes return `jsonify(vars(task))` — relies on `Task` being a plain dataclass.
- Not-found responses use `{"error": "..."}` with 404.
- `request.get_json(silent=True) or {}` is the pattern for tolerating missing/invalid JSON bodies.
- No auth, no persistence — everything resets when the process restarts (and explicitly in tests via the `client` fixture).

## Testing
```bash
pytest -v
```
Run from the `taskflow-api/` directory. On a fresh clone: 5 passing, 1 failing (`test_create_task_rejects_empty_title` in [tests/test_tasks.py](tests/test_tasks.py:45)) — it documents a known validation bug.

## Known issue (active ticket)
`POST /tasks` accepts empty or missing `title` and silently creates a blank task ([app/routes.py:16-22](app/routes.py:16)). Expected: `400 Bad Request` for empty/missing title, `201` unchanged for valid titles. See `TICKET.md`.
