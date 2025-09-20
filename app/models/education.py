"""Education model"""
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.profile import Profile


class EducationBase(SQLModel):
    """Base education fields"""
    degree_type: str = Field(max_length=100)
    university_name: str = Field(max_length=200)
    order_index: int = Field(default=0)


class Education(EducationBase, table=True):
    """Education database model"""
    __tablename__ = "education"

    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profiles.id")

    # Relationship
    profile: Optional["Profile"] = Relationship(back_populates="education")


class EducationRead(EducationBase):
    """Schema for reading education records"""
    id: int
    profile_id: int
