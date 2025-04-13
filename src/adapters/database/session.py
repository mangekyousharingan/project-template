from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from typing import Generator

from src.adapters.database.models import Base
from src.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 