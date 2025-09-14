"""Profile routers"""
from fastapi import APIRouter, HTTPException, status
from app.dependencies import ProfileServiceDep
from app.models import ProfileRead

router = APIRouter(prefix="/profile", tags=["profile"])


# noinspection PyTypeHints
@router.get("/", response_model=ProfileRead)
def get_profile(service: ProfileServiceDep):
    """Get the site's profile (first profile in database)"""
    profile = service.get_first_profile()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return profile


# noinspection PyTypeHints
@router.get("/{profile_id}", response_model=ProfileRead)
def get_profile_by_id(profile_id: int, service: ProfileServiceDep):
    """Get a specific profile by ID"""
    profile = service.get_profile(profile_id)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return profile
