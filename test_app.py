from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_add():
    response = client.get("/add?a=1&b=2")
    assert response.status_code == 200
    assert response.json() == {"result": 3}

def test_sub():
    response = client.get("/sub?a=4&b=2")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_mul():
    response = client.get("/mul?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_div():
    response = client.get("/div?a=6&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_sqrt():
    response = client.get("/sqrt?a=4")
    assert response.status_code == 200
    assert response.json() == {"result": 2}
