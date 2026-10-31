from fastapi import FastAPI, HTTPException, status
from models.models import Sheep
from models.db import db

app = FastAPI()

@app.get("/sheep/{sheep_id}", response_model=Sheep)
def read_sheep(sheep_id: int):
    sheep = db.get_sheep(sheep_id)
    if sheep is None:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return sheep


@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    # Check if the sheep ID already exists to avoid duplicates
    if sheep.id in db.sheep_data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")

    # Add the new sheep to the database
    db.sheep_data[sheep.id] = sheep
    return sheep