from fastapi import FastAPI, HTTPException, status
from typing import List
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

@app.delete("/sheep/{sheep_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(sheep_id: int):
    deleted = db.delete_sheep(sheep_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Sheep not found")


@app.put("/sheep/{sheep_id}", response_model=Sheep)
def update_sheep(sheep_id: int, sheep: Sheep):
    updated = db.update_sheep(sheep_id, sheep)
    if updated is None:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return updated


@app.get("/sheep/", response_model=List[Sheep])
def read_all_sheep():
    return db.get_all_sheep()


@app.get("/sheep/{sheep_id}", response_model=Sheep)
def read_sheep(sheep_id: int):
    ...