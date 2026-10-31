from fastapi.testclient import TestClient
from main import app

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