# import fastapi.testclient
#
# import app.main as dashboard
#
#
# def test_dashboard_success():
#     client = fastapi.testclient.TestClient(dashboard.app)
#     response = client.get("/dashboard")
#
#     assert response.status_code == 200
#     assert "X-Request-Id" in response.headers
#     assert len(response.headers["X-Request-Id"]) > 0
#
#
# def test_dashboard_failure():
#     client = fastapi.testclient.TestClient(dashboard.app)
#     response = client.post("/dashboard")
#     assert response.status_code == 405
