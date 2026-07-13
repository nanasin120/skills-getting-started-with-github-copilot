from fastapi.testclient import TestClient

from src.app import app, activities


def setup_function():
    activities["Chess Club"]["participants"] = ["michael@mergington.edu", "daniel@mergington.edu"]


def test_unregister_participant_removes_email_from_activity():
    client = TestClient(app)

    response = client.delete("/activities/Chess Club/signup?email=michael@mergington.edu")

    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered michael@mergington.edu from Chess Club"

    refreshed = client.get("/activities").json()
    assert "michael@mergington.edu" not in refreshed["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in refreshed["Chess Club"]["participants"]
