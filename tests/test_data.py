from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calc_add():
    response = client.get("/calc", params={"a": 2, "b": 3, "op": "add"})
    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_calc_sub():
    response = client.get("/calc", params={"a": 5, "b": 2, "op": "sub"})
    assert response.status_code == 200
    assert response.json()["result"] == 3

def test_calc_mul():
    response = client.get("/calc", params={"a": 4, "b": 3, "op": "mul"})
    assert response.status_code == 200
    assert response.json()["result"] == 12

def test_calc_div():
    response = client.get("/calc", params={"a": 12, "b": 4, "op": "div"})
    assert response.status_code == 200
    assert response.json()["result"] == 3

def test_calc_div_zero():
    response = client.get("/calc", params={"a": 1, "b": 0, "op": "div"})
    assert response.status_code == 200
    assert response.json()["error"] == "Division by zero"

def test_calc_invalid_op():
    response = client.get("/calc", params={"a": 1, "b": 2, "op": "mod"})
    assert response.status_code == 200
    assert response.json()["error"] == "Invalid operation"
