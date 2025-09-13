"""Authentication dependencies for FastAPI"""
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi_azure_auth.user import User
from app.auth.azure_ad import azure_scheme, user_has_admin_access
from app.config import settings


def get_current_user(user: User = Depends(azure_scheme)) -> User:
    """Get current authenticated user from Azure AD"""
    if not azure_scheme:
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Azure AD authentication not configured. Please set AZURE_TENANT_ID and AZURE_CLIENT_ID environment variables."
        )
    return user


def verify_admin_token(current_user: User = Depends(get_current_user)) -> User:
    """Verify that the current user has admin access"""
    if not user_has_admin_access(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required. Please ensure you have the 'Admin' role or 'admin' scope."
        )
    
    return current_user


def get_optional_user() -> Optional[User]:
    """Optional user dependency - returns None if Azure AD is not configured"""
    if not azure_scheme:
        return None
    
    # This would need to be implemented differently in a real scenario
    # For now, we'll return None for optional authentication
    return None


# Fallback authentication for development when Azure AD is not configured
def development_auth_fallback():
    """Fallback authentication for development environments"""
    if settings.is_azure_ad_configured or settings.is_azure_b2c_configured:
        return get_current_user
    
    # In development without Azure AD, we can allow admin access
    # This should NEVER be used in production
    def mock_admin_user():
        class MockUser:
            def __init__(self):
                self.name = "Development Admin"
                self.preferred_username = "dev-admin"
                self.roles = ["Admin"]
                self.scp = f"api://{settings.AZURE_CLIENT_ID}/admin" if settings.AZURE_CLIENT_ID else "admin"
        
        return MockUser()
    
    return mock_admin_user