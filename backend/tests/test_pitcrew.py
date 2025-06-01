from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_pitcrew_placeholder():
    resp = client.post("/api/pitcrew/", json={"symptoms": {"noise": "clunk"}})
    assert resp.status_code == 200
    data = resp.json()
    assert "diagnosis" in data
