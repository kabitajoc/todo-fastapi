from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_todo():
    response = client.post(
        "/api/todos", json={"title": "Test Todo", "description": "Test Description"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Todo"
