from fastapi import FastAPI
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{sheep_id}", response_model=Sheep)
def read_sheep(id: int):
    return db.get_sheep(id)

