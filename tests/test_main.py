from fastapi.testclient import TestClient
from main import app
from models.db import db
client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
          "id": 1,
          "name": "Spice",
          "breed": "Gotland",
          "sex": "ewe"
    }

def test_add_sheep():
    new_sheep = {
          "id": 7,
          "name": "New Sheep",
          "breed": "Test",
          "sex": "m"
    }
    response = client.post("/sheep/", json=new_sheep)
    assert response.status_code == 200
    assert response.json() == new_sheep
    response = client.get("/sheep/7")
    assert response.json() == new_sheep

def test_delete_sheep():
    delete_sheep = {
      "id": 1,
      "name": "Spice",
      "breed": "Gotland",
      "sex": "ewe"
    }
    response = client.delete("/sheep/1")
    assert response.status_code == 200
    assert response.json() == delete_sheep

def test_update_sheep():
    update_sheep = {
      "id": 1,
      "name": "Spice-Update",
      "breed": "Gotland",
      "sex": "ewe"
    }
    response = client.put("/sheep/1", json=update_sheep)
    assert response.status_code == 200
    assert response.json() == update_sheep

def test_read_all_sheep():
    response = client.get("/sheep/")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == db