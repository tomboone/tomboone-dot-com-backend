"""Base repository"""
from abc import ABC
from typing import Generic, TypeVar, Type, Optional, List
from sqlmodel import Session, select, SQLModel

T = TypeVar('T', bound=SQLModel)


class BaseRepository(Generic[T], ABC):
    """Base repository"""
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def get(self, base_id: int) -> Optional[T]:
        """Get object with given id"""
        return self.db.get(self.model, base_id)

    def get_all(self) -> List[T]:
        """Get all objects"""
        statement = select(self.model)
        return list(self.db.exec(statement).all())
