from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root_returns_running_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}


def test_readiness_endpoint():
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_demo_failure_returns_500():
    response = client.get("/demo/failure")
    assert response.status_code == 500
    assert response.json()["detail"] == "Intentional demo failure for reliability testing"
