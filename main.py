from fastapi import FastAPI, HTTPException
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep, tags=["Sheep"])
def read_sheep(id: int):
    return db.get_sheep(id)

@app.post("/sheep/", response_model=Sheep,tags=["Sheep"])
def add_sheep(new_sheep: Sheep):
    db.add_sheep(new_sheep)
    return new_sheep

@app.delete("/sheep/{id}", response_model=Sheep,tags=["Sheep"])
def delete_sheep(id: int):
    sheep = db.delete_sheep(id)
    if sheep is None:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return sheep
