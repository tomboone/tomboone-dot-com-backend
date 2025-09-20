"""Repository for Work Experience"""
from typing import List
from sqlmodel import Session, select
from app.models.work_experience import WorkExperience
from app.repositories.base import BaseRepository


class WorkExperienceRepository(BaseRepository[WorkExperience]):
    """Repository for Work Experience"""
    def __init__(self, db: Session):
        super().__init__(db, WorkExperience)

    def get_by_profile_id(self, profile_id: int) -> List[WorkExperience]:
        """Get Work Experience by Profile ID"""
        statement = (
            select(self.model)
            .where(self.model.profile_id == profile_id)
            .order_by(self.model.order_index)  # type: ignore[arg-type]
        )
        return list(self.db.exec(statement).all())
