"""In-memory data model for tasks.

This intentionally uses a simple in-memory store (no database) to keep the
demo repo self-contained and dependency-free.
"""
from dataclasses import dataclass, field
from itertools import count
from typing import Dict, Optional

_id_counter = count(1)


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TaskStore:
    """A minimal in-memory repository for Task objects."""

    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}

    def create(self, title: str) -> Task:
        task_id = next(_id_counter)
        task = Task(id=task_id, title=title)
        self._tasks[task_id] = task
        return task

    def list(self) -> list[Task]:
        return list(self._tasks.values())

    def get(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def update(self, task_id: int, **fields) -> Optional[Task]:
        task = self._tasks.get(task_id)
        if task is None:
            return None
        for key, value in fields.items():
            setattr(task, key, value)
        return task

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None


# Module-level singleton store used by the routes.
store = TaskStore()
