"""Profile routers"""
from typing import Dict, Any
from fastapi import APIRouter, HTTPException, status, Depends
from app.dependencies import ProfileServiceDep
from app.auth.dependencies import verify_admin_token
from app.models import (
    ProfileCreate,
    ProfileUpdate,
    ProfileRead,
)

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


# noinspection PyTypeHints
@router.post("/", response_model=ProfileRead, status_code=status.HTTP_201_CREATED)
def create_profile(
    profile_data: ProfileCreate, 
    service: ProfileServiceDep,
    current_user = Depends(verify_admin_token)
):
    """Create a new profile"""
    try:
        profile = service.create_profile(profile_data)
        return profile
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating profile: {str(e)}"
        )


# noinspection PyTypeHints
@router.put("/{profile_id}", response_model=ProfileRead)
def update_profile(
    profile_id: int, 
    profile_data: ProfileUpdate, 
    service: ProfileServiceDep,
    current_user = Depends(verify_admin_token)
):
    """Update an existing profile"""
    profile = service.update_profile(profile_id, profile_data)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return profile


# noinspection PyTypeHints
@router.delete("/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(
    profile_id: int, 
    service: ProfileServiceDep,
    current_user = Depends(verify_admin_token)
):
    """Delete a profile"""
    success = service.delete_profile(profile_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )


# noinspection PyTypeHints
@router.post("/full", response_model=ProfileRead, status_code=status.HTTP_201_CREATED)
def create_full_profile(
    profile_data: Dict[str, Any], 
    service: ProfileServiceDep,
    current_user = Depends(verify_admin_token)
):
    """Create a complete profile with all related data (work experience, education, projects, consulting work)"""
    try:
        profile = service.create_full_profile(profile_data)
        return profile
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating full profile: {str(e)}"
        )


# noinspection PyTypeHints
@router.put("/full/{profile_id}", response_model=ProfileRead)
def update_full_profile(
    profile_id: int, 
    profile_data: Dict[str, Any], 
    service: ProfileServiceDep,
    current_user = Depends(verify_admin_token)
):
    """Update a complete profile with all related data"""
    try:
        profile = service.update_full_profile(profile_id, profile_data)
        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profile not found"
            )
        return profile
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error updating full profile: {str(e)}"
        )
