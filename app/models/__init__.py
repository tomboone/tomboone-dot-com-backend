"""Models for profiles"""
from app.models.consulting_work import (
    ConsultingWork,
    ConsultingWorkRead,
)
from app.models.education import (
    Education,
    EducationRead,
)
from app.models.profile import (
    Profile,
    ProfileRead,
)
from app.models.project import (
    Project,
    ProjectRead,
)
from app.models.work_experience import (
    WorkExperience,
    WorkExperienceRead,
)

__all__ = [
    "ConsultingWork",
    "Education",
    "Profile",
    "Project",
    "WorkExperience",
    "ConsultingWorkRead",
    "EducationRead",
    "ProfileRead",
    "ProjectRead",
    "WorkExperienceRead",
]

# Rebuild models to resolve forward references
ProfileRead.model_rebuild()
ProjectRead.model_rebuild()
WorkExperienceRead.model_rebuild()
ConsultingWorkRead.model_rebuild()
EducationRead.model_rebuild()
