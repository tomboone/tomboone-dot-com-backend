"""Profile Service"""
from typing import Optional, Dict, Any
from sqlmodel import Session
from app.models import (
    Profile,
    ProfileCreate,
    ProfileUpdate,
    WorkExperienceCreate,
    EducationCreate,
    ProjectCreate,
    ConsultingWorkCreate,
)
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

    def create_profile(self, profile_data: ProfileCreate) -> Profile:
        """Create a new profile"""
        return self.profile_repo.create(profile_data.model_dump())

    def update_profile(self, profile_id: int, profile_data: ProfileUpdate) -> Optional[Profile]:
        """Update an existing profile"""
        update_data = profile_data.model_dump(exclude_unset=True)
        if not update_data:
            return self.profile_repo.get(profile_id)
        
        return self.profile_repo.update(profile_id, update_data)

    def delete_profile(self, profile_id: int) -> bool:
        """Delete a profile and all related data"""
        return self.profile_repo.delete(profile_id)

    def create_full_profile(self, profile_data: Dict[str, Any]) -> Profile:
        """Create a complete profile with all related data"""
        # Extract profile data
        profile_dict = {
            "name": profile_data.get("name"),
            "profession": profile_data.get("profession"),
            "email": profile_data.get("email"),
            "github_link": profile_data.get("github_link"),
            "linkedin_link": profile_data.get("linkedin_link"),
            "summary_text": profile_data.get("summary_text"),
        }
        
        # Create the profile
        profile = self.profile_repo.create(profile_dict)

        # Create related data if provided
        if "work_experiences" in profile_data:
            for work_exp_data in profile_data["work_experiences"]:
                work_exp_data["profile_id"] = profile.id
                work_exp = WorkExperienceCreate(**work_exp_data)
                self.work_experience_repo.create(work_exp.model_dump())

        if "education" in profile_data:
            for edu_data in profile_data["education"]:
                edu_data["profile_id"] = profile.id
                education = EducationCreate(**edu_data)
                self.education_repo.create(education.model_dump())

        if "projects" in profile_data:
            for project_data in profile_data["projects"]:
                project_data["profile_id"] = profile.id
                project = ProjectCreate(**project_data)
                self.project_repo.create(project.model_dump())

        if "consulting_work" in profile_data:
            for consulting_data in profile_data["consulting_work"]:
                consulting_data["profile_id"] = profile.id
                consulting = ConsultingWorkCreate(**consulting_data)
                self.consulting_work_repo.create(consulting.model_dump())

        # Return the profile with all relations loaded
        self.session.commit()
        return self.profile_repo.get_with_relations(profile.id)

    def update_full_profile(self, profile_id: int, profile_data: Dict[str, Any]) -> Optional[Profile]:
        """Update a complete profile with all related data"""
        profile = self.profile_repo.get(profile_id)
        if not profile:
            return None

        # Update profile data
        profile_fields = {
            "name", "profession", "email", "github_link", 
            "linkedin_link", "summary_text"
        }
        profile_updates = {k: v for k, v in profile_data.items() if k in profile_fields}
        
        if profile_updates:
            self.profile_repo.update(profile_id, profile_updates)

        # Update related data - replace all
        if "work_experiences" in profile_data:
            self.work_experience_repo.delete_by_profile_id(profile_id)
            for work_exp_data in profile_data["work_experiences"]:
                work_exp_data["profile_id"] = profile_id
                work_exp = WorkExperienceCreate(**work_exp_data)
                self.work_experience_repo.create(work_exp.model_dump())

        if "education" in profile_data:
            self.education_repo.delete_by_profile_id(profile_id)
            for edu_data in profile_data["education"]:
                edu_data["profile_id"] = profile_id
                education = EducationCreate(**edu_data)
                self.education_repo.create(education.model_dump())

        if "projects" in profile_data:
            self.project_repo.delete_by_profile_id(profile_id)
            for project_data in profile_data["projects"]:
                project_data["profile_id"] = profile_id
                project = ProjectCreate(**project_data)
                self.project_repo.create(project.model_dump())

        if "consulting_work" in profile_data:
            self.consulting_work_repo.delete_by_profile_id(profile_id)
            for consulting_data in profile_data["consulting_work"]:
                consulting_data["profile_id"] = profile_id
                consulting = ConsultingWorkCreate(**consulting_data)
                self.consulting_work_repo.create(consulting.model_dump())

        # Return the updated profile with all relations
        self.session.commit()
        return self.profile_repo.get_with_relations(profile_id)
