"""Project model"""
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.profile import Profile


class ProjectBase(SQLModel):
    """Base project fields"""
    title: str = Field(max_length=200)
    description: str
    order_index: int = Field(default=0)


class Project(ProjectBase, table=True):
    """Project database model"""
    __tablename__ = "projects"

    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profiles.id")

    # Relationship
    profile: Optional["Profile"] = Relationship(back_populates="projects")


class ProjectCreate(ProjectBase):
    """Schema for creating projects"""
    pass


class ProjectUpdate(SQLModel):
    """Schema for updating projects"""
    title: Optional[str] = Field(default=None, max_length=200)
    description: Optional[str] = None
    order_index: Optional[int] = None


class ProjectRead(ProjectBase):
    """Schema for reading projects"""
    id: int
    profile_id: int
