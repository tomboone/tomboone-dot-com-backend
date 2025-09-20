"""Work Experience model"""
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.profile import Profile


class WorkExperienceBase(SQLModel):
    """Base work experience fields"""
    employer_name: str = Field(max_length=200)
    position: str = Field(max_length=200)
    order_index: int = Field(default=0)


class WorkExperience(WorkExperienceBase, table=True):
    """Work Experience database model"""
    __tablename__ = "work_experiences"

    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profiles.id")

    # Relationship
    profile: Optional["Profile"] = Relationship(back_populates="work_experiences")


class WorkExperienceRead(WorkExperienceBase):
    """Schema for reading work experiences"""
    id: int
    profile_id: int
