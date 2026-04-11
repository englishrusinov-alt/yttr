# import fastapi.testclient
#
# import app.health as health
#
#
# def test_health_success():
#     client = fastapi.testclient.TestClient(health.app)
#     response = client.get("/health")
#     assert response.status_code == 200
#
#
# def test_health_failure():
#     client = fastapi.testclient.TestClient(health.app)
#     response = client.post("/health")
#     assert response.status_code == 200
