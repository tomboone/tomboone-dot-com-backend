"""Consulting Work Model"""
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.profile import Profile


class ConsultingWorkBase(SQLModel):
    """Base consulting work fields"""
    employer_name: str = Field(max_length=200)
    position: str = Field(max_length=200)
    order_index: int = Field(default=0)


class ConsultingWork(ConsultingWorkBase, table=True):
    """Consulting Work database model"""
    __tablename__ = "consulting_work"

    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profiles.id")

    # Relationship
    profile: Optional["Profile"] = Relationship(back_populates="consulting_work")


class ConsultingWorkRead(ConsultingWorkBase):
    """Schema for reading consulting work records"""
    id: int
    profile_id: int
