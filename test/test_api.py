from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_health():
    response = client.get("/health")

    assert response.status_code == 200

def test_get_anagrams():
    response = client.get("/anagrams/rots")
    assert response.status_code == 200
    data = response.json()
    assert "rots" in data["anagrams"]
    assert "sort" in data["anagrams"]

def test_no_anagrams():
    response = client.get("/anagrams/abc")

    assert response.status_code == 404