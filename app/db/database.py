"""Database configuration"""
from typing import Dict, Any
from sqlmodel import create_engine, Session
from app.config import settings

# Export DATABASE_URL for Alembic
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Database engine
connect_args: Dict[str, Any] = {}
if "sqlite" in settings.DATABASE_URL:
    connect_args = {"check_same_thread": False}
elif "mysql" in settings.DATABASE_URL:
    connect_args = {
        "charset": "utf8mb4",
    }

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)


def get_session():
    """Get database session"""
    with Session(engine) as session:
        yield session
