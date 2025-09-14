"""Repository for Project"""
from typing import List
from sqlmodel import Session, select
from app.models.project import Project
from app.repositories.base import BaseRepository


class ProjectRepository(BaseRepository[Project]):
    """Project repository"""
    def __init__(self, db: Session):
        super().__init__(db, Project)

    def get_by_profile_id(self, profile_id: int) -> List[Project]:
        """Get project by profile id"""
        statement = (
            select(self.model)
            .where(self.model.profile_id == profile_id)
            .order_by(self.model.order_index)  # type: ignore[arg-type]
        )
        return list(self.db.exec(statement).all())
