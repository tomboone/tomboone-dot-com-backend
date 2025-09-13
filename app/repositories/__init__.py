"""Repository classes"""
from app.repositories.base import BaseRepository
from app.repositories.profile import ProfileRepository
from app.repositories.work_experience import WorkExperienceRepository
from app.repositories.education import EducationRepository
from app.repositories.project import ProjectRepository
from app.repositories.consulting_work import ConsultingWorkRepository

__all__ = [
    "BaseRepository",
    "ProfileRepository",
    "WorkExperienceRepository",
    "EducationRepository",
    "ProjectRepository",
    "ConsultingWorkRepository",
]
