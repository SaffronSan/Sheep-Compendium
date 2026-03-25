from fastapi import FastAPI
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