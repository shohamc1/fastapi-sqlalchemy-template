from sqlalchemy.orm import Session
import schemas
from models import User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(
        email=user.email, first_name=user.first_name, last_name=user.last_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
