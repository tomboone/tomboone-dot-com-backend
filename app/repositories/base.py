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

    def create(self, obj_data: dict) -> T:
        """Create new object with given data"""
        db_obj = self.model(**obj_data)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get(self, base_id: int) -> Optional[T]:
        """Get object with given id"""
        return self.db.get(self.model, base_id)

    def get_all(self) -> List[T]:
        """Get all objects"""
        statement = select(self.model)
        return list(self.db.exec(statement).all())

    def update(self, base_id: int, obj_data: dict) -> Optional[T]:
        """Update object with given id"""
        db_obj = self.get(base_id)
        if db_obj:
            for key, value in obj_data.items():
                setattr(db_obj, key, value)
            self.db.commit()
            self.db.refresh(db_obj)
        return db_obj

    def delete(self, base_id: int) -> bool:
        """Delete object with given id"""
        db_obj = self.get(base_id)
        if db_obj:
            self.db.delete(db_obj)
            self.db.commit()
            return True
        return False
