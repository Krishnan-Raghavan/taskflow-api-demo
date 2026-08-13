"""HTTP routes for the TaskFlow API.

NOTE FOR DEMO FACILITATOR:
The POST /tasks endpoint below does not validate that "title" is present
or non-empty. This is intentional -- it's the bug Claude Code will find
and fix live during the demo. See tests/test_tasks.py::test_create_task_rejects_empty_title
for the failing test that exposes it.
"""
from flask import Blueprint, jsonify, request

from app.models import store

bp = Blueprint("tasks", __name__)


@bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title", "")
    # BUG: no validation here -- empty/missing titles are silently accepted.
    task = store.create(title=title)
    return jsonify(vars(task)), 201


@bp.route("/tasks", methods=["GET"])
def list_tasks():
    tasks = store.list()
    return jsonify([vars(t) for t in tasks]), 200


@bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id: int):
    task = store.get(task_id)
    if task is None:
        return jsonify({"error": "task not found"}), 404
    return jsonify(vars(task)), 200


@bp.route("/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id: int):
    data = request.get_json(silent=True) or {}
    fields = {}
    if "title" in data:
        fields["title"] = data["title"]
    if "done" in data:
        fields["done"] = data["done"]
    task = store.update(task_id, **fields)
    if task is None:
        return jsonify({"error": "task not found"}), 404
    return jsonify(vars(task)), 200


@bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id: int):
    deleted = store.delete(task_id)
    if not deleted:
        return jsonify({"error": "task not found"}), 404
    return "", 204
