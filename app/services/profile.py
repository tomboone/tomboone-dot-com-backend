"""Profile Service"""
from typing import Optional
from sqlmodel import Session
from app.models import Profile
from app.repositories import (
    ProfileRepository,
    WorkExperienceRepository,
    EducationRepository,
    ProjectRepository,
    ConsultingWorkRepository,
)


class ProfileService:
    """Profile Service"""
    def __init__(self, session: Session):
        self.session = session
        self.profile_repo = ProfileRepository(session)
        self.work_experience_repo = WorkExperienceRepository(session)
        self.education_repo = EducationRepository(session)
        self.project_repo = ProjectRepository(session)
        self.consulting_work_repo = ConsultingWorkRepository(session)

    def get_profile(self, profile_id: int) -> Optional[Profile]:
        """Get profile by ID with all related data"""
        return self.profile_repo.get_with_relations(profile_id)

    def get_first_profile(self) -> Optional[Profile]:
        """Get the first (and likely only) profile with all related data"""
        return self.profile_repo.get_first_profile_with_relations()
