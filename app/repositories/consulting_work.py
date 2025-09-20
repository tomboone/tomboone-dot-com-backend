"""Repository for consulting work"""
from typing import List
from sqlmodel import Session, select
from app.models.consulting_work import ConsultingWork
from app.repositories.base import BaseRepository


class ConsultingWorkRepository(BaseRepository[ConsultingWork]):
    """Repository for consulting work"""
    def __init__(self, db: Session):
        super().__init__(db, ConsultingWork)

    def get_by_profile_id(self, profile_id: int) -> List[ConsultingWork]:
        """Get consulting work by profile id"""
        statement = (
            select(self.model)
            .where(self.model.profile_id == profile_id)
            .order_by(self.model.order_index)  # type: ignore[arg-type]
        )
        return list(self.db.exec(statement).all())
