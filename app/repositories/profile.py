"""Repository for Profile"""
from typing import Optional, List
from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from app.models.profile import Profile
from app.repositories.base import BaseRepository


# noinspection PyTypeChecker
class ProfileRepository(BaseRepository[Profile]):
    """Repository for Profile"""
    def __init__(self, db: Session):
        super().__init__(db, Profile)

    def get_with_relations(self, profile_id: int) -> Optional[Profile]:
        """Get profile with given id"""
        statement = (
            select(self.model)
            .options(
                joinedload(self.model.work_experiences),  # type: ignore[arg-type]
                joinedload(self.model.education),  # type: ignore[arg-type]
                joinedload(self.model.projects),  # type: ignore[arg-type]
                joinedload(self.model.consulting_work)  # type: ignore[arg-type]
            )
            .where(self.model.id == profile_id)
        )
        return self.db.exec(statement).first()

    def get_all_with_relations(self) -> List[Profile]:
        """Get all profiles"""
        statement = (
            select(self.model)
            .options(
                joinedload(self.model.work_experiences),  # type: ignore[arg-type]
                joinedload(self.model.education),  # type: ignore[arg-type]
                joinedload(self.model.projects),  # type: ignore[arg-type]
                joinedload(self.model.consulting_work)  # type: ignore[arg-type]
            )
        )
        return list(self.db.exec(statement).all())

    def get_first_profile(self) -> Optional[Profile]:
        """Get the first (and likely only) profile"""
        statement = select(self.model)
        return self.db.exec(statement).first()

    def get_first_profile_with_relations(self) -> Optional[Profile]:
        """Get the first profile with all related data"""
        statement = (
            select(self.model)
            .options(
                joinedload(self.model.work_experiences),  # type: ignore[arg-type]
                joinedload(self.model.education),  # type: ignore[arg-type]
                joinedload(self.model.projects),  # type: ignore[arg-type]
                joinedload(self.model.consulting_work)  # type: ignore[arg-type]
            )
        )
        return self.db.exec(statement).first()
