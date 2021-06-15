from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import cruds
import schemas
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from endpoints.User import *


@app.get("/")
def hello():
    return "Hello"
