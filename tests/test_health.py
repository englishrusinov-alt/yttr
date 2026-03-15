import app.health as health
import fastapi.testclient
def test_health_success():
    client = fastapi.testclient.TestClient(health.app)
    response  = client.get("/health")
    assert response.status_code == 200
def test_health_failure():
    client = fastapi.testclient.TestClient(health.app)
    response = client.post("/health")
    assert response.status_code == 200