from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends

from main import app, get_db
import schemas
import cruds


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return cruds.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = cruds.get_users(db)
    return users
