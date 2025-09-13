"""Repository for Education"""
from typing import List
from sqlmodel import Session, select
from app.models.education import Education
from app.repositories.base import BaseRepository


class EducationRepository(BaseRepository[Education]):
    """Repository for Education"""
    def __init__(self, db: Session):
        super().__init__(db, Education)

    def get_by_profile_id(self, profile_id: int) -> List[Education]:
        """Get education by profile id"""
        statement = (
            select(self.model)
            .where(self.model.profile_id == profile_id)
            .order_by(self.model.order_index)
        )
        return list(self.db.exec(statement).all())

    def delete_by_profile_id(self, profile_id: int) -> int:
        """Delete all education records for a profile and return count"""
        statement = select(self.model).where(self.model.profile_id == profile_id)
        items = self.db.exec(statement).all()
        count = len(items)
        for item in items:
            self.db.delete(item)
        self.db.commit()
        return count
