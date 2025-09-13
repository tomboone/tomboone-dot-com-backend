"""Dependencies"""
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from app.db.database import get_session
from app.services import ProfileService

# Database session dependency
SessionDep = Annotated[Session, Depends(get_session)]


def get_profile_service(session: SessionDep) -> ProfileService:
    """Get profile service with database session"""
    return ProfileService(session)


# Profile service dependency
ProfileServiceDep = Annotated[ProfileService, Depends(get_profile_service)]
