import pytest
from fastapi.testclient import TestClient

from api.api import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_task(client):
    task_payload = {"name": "Test Task", "date": None, "completed": False}
    response = client.post("/tasks", json=task_payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Task added successfully"}
