"""Profile model"""
import datetime
from typing import TYPE_CHECKING, Optional, List
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models import Project, WorkExperience, ConsultingWork, Education


class ProfileBase(SQLModel):
    """Base profile fields for validation"""
    name: str = Field(max_length=100)
    profession: str = Field(max_length=150)
    email: str = Field(max_length=255)
    github_link: Optional[str] = Field(default=None, max_length=255)
    linkedin_link: Optional[str] = Field(default=None, max_length=255)
    summary_text: Optional[str] = None


class Profile(ProfileBase, table=True):
    """Profile database model"""
    __tablename__ = "profiles"

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.UTC))
    updated_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.UTC))

    # Relationships
    projects: List["Project"] = Relationship(back_populates="profile", cascade_delete=True)
    work_experiences: List["WorkExperience"] = Relationship(back_populates="profile", cascade_delete=True)
    consulting_work: List["ConsultingWork"] = Relationship(back_populates="profile", cascade_delete=True)
    education: List["Education"] = Relationship(back_populates="profile", cascade_delete=True)


class ProfileCreate(ProfileBase):
    """Schema for creating profiles"""
    pass


class ProfileUpdate(SQLModel):
    """Schema for updating profiles"""
    name: Optional[str] = Field(default=None, max_length=100)
    profession: Optional[str] = Field(default=None, max_length=150)
    email: Optional[str] = Field(default=None, max_length=255)
    github_link: Optional[str] = Field(default=None, max_length=255)
    linkedin_link: Optional[str] = Field(default=None, max_length=255)
    summary_text: Optional[str] = None


class ProfileRead(ProfileBase):
    """Schema for reading profiles"""
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
