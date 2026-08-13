"""Test suite for the TaskFlow API.

test_create_task_rejects_empty_title is EXPECTED TO FAIL on a fresh clone.
It documents the behavior the API should have, exposing the validation bug
in app/routes.py::create_task. This is the test Claude Code should make
pass during the live demo.
"""


def test_create_task_happy_path(client):
    resp = client.post("/tasks", json={"title": "Write demo script"})
    assert resp.status_code == 201
    body = resp.get_json()
    assert body["title"] == "Write demo script"
    assert body["done"] is False


def test_list_tasks(client):
    client.post("/tasks", json={"title": "Task A"})
    client.post("/tasks", json={"title": "Task B"})
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 2


def test_get_missing_task_returns_404(client):
    resp = client.get("/tasks/9999")
    assert resp.status_code == 404


def test_update_task_marks_done(client):
    created = client.post("/tasks", json={"title": "Ship feature"}).get_json()
    resp = client.patch(f"/tasks/{created['id']}", json={"done": True})
    assert resp.status_code == 200
    assert resp.get_json()["done"] is True


def test_delete_task(client):
    created = client.post("/tasks", json={"title": "Temp task"}).get_json()
    resp = client.delete(f"/tasks/{created['id']}")
    assert resp.status_code == 204
    assert client.get(f"/tasks/{created['id']}").status_code == 404


def test_create_task_rejects_empty_title(client):
    """EXPECTED TO FAIL until the validation bug is fixed."""
    resp = client.post("/tasks", json={"title": ""})
    assert resp.status_code == 400

    resp_missing = client.post("/tasks", json={})
    assert resp_missing.status_code == 400
