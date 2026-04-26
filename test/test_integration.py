import httpx

def test_health(server):
    response = httpx.get("http://localhost:8000/health")
    assert response.status_code == 200

def test_get_anagrams(server):
    response = httpx.get("http://localhost:8000/anagrams/rots")
    assert response.status_code == 200

def test_no_anagrams(server):
    response = httpx.get("http://localhost:8000/anagrams/abc")
    assert response.status_code == 404