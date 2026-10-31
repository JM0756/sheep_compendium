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
        "sex": "ewe",
    }

def test_add_sheep():
    # Prepare the new sheep data in a dictionary format
    new_sheep = {
        "id": 24,
        "name": "Lessie",
        "breed": "Lincoln Longwool",
        "sex": "ram"
    }

    # Send a POST request to the endpoint "/sheep" with the new sheep data
    response = client.post("/sheep/", json=new_sheep)

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # Assert that the response JSON matches the new sheep data
    assert response.json() == new_sheep

    # Verify that the sheep was actually added to the database by retrieving it by ID
    get_response = client.get("/sheep/24")
    assert get_response.json() == new_sheep


def test_delete_sheep():
    # Confirm the sheep exists before deleting
    response = client.get("/sheep/2")
    assert response.status_code == 200

    # Send a DELETE request
    response = client.delete("/sheep/2")
    assert response.status_code == 204

    # Confirm the sheep is gone
    response = client.get("/sheep/2")
    assert response.status_code == 404


def test_update_sheep():
    updated_data = {
        "id": 3,
        "name": "Lamb Chop",
        "breed": "Dorset",
        "sex": "wether"
    }

    response = client.put("/sheep/3", json=updated_data)
    assert response.status_code == 200
    assert response.json() == updated_data

    # Confirm the change persisted
    get_response = client.get("/sheep/3")
    assert get_response.json() == updated_data


def test_read_all_sheep():
    response = client.get("/sheep/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == len(db.sheep_data)