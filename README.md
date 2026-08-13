# TaskFlow API

A tiny Flask task-management REST API, built as a **Claude Code demo repo**.

## Endpoints

- `POST /tasks` — create a task (`{"title": "..."}`)
- `GET /tasks` — list all tasks
- `GET /tasks/<id>` — get one task
- `PATCH /tasks/<id>` — update a task (`title` and/or `done`)
- `DELETE /tasks/<id>` — delete a task

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run tests

```bash
pytest -v
```

You should see **5 passing, 1 failing** on a fresh clone. The failing test,
`test_create_task_rejects_empty_title`, documents a validation bug: the API
currently accepts empty/missing task titles instead of returning `400`.

## Run the app

```bash
python -m app.main
```
