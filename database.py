from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils import create_connection_string
import os


if os.getenv("PRODUCTION"):
    DATABASE_URL = create_connection_string()
    engine = create_engine(DATABASE_URL)
else:
    DATABASE_URL = "sqlite:///./sql_app.db"
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# connect args only needed for sqlite

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
