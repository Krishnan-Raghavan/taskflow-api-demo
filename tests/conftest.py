import pytest

from app.main import create_app
from app.models import store


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    # Reset in-memory store so tests don't leak state into each other.
    store._tasks.clear()
    with app.test_client() as c:
        yield c
