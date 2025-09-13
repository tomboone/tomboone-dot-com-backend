"""Azure AD authentication setup"""
from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer, MultiTenantAzureAuthorizationCodeBearer
from fastapi_azure_auth.user import User
from app.config import settings
from typing import Optional


def create_azure_auth_scheme() -> Optional[SingleTenantAzureAuthorizationCodeBearer]:
    """Create Azure AD authentication scheme"""
    if not settings.is_azure_ad_configured:
        return None
    
    return SingleTenantAzureAuthorizationCodeBearer(
        app_id=settings.AZURE_CLIENT_ID,
        tenant_id=settings.AZURE_TENANT_ID,
        scopes={
            f"api://{settings.AZURE_CLIENT_ID}/admin": "Admin access to portfolio API",
            f"api://{settings.AZURE_CLIENT_ID}/read": "Read access to portfolio API"
        }
    )


def create_azure_b2c_auth_scheme() -> Optional[SingleTenantAzureAuthorizationCodeBearer]:
    """Create Azure AD B2C authentication scheme"""
    if not settings.is_azure_b2c_configured:
        return None
    
    return SingleTenantAzureAuthorizationCodeBearer(
        app_id=settings.AZURE_CLIENT_ID,
        tenant_id=f"{settings.AZURE_B2C_TENANT_NAME}.onmicrosoft.com",
        policy=settings.AZURE_B2C_POLICY_NAME,
        scopes={
            f"https://{settings.AZURE_B2C_TENANT_NAME}.onmicrosoft.com/{settings.AZURE_CLIENT_ID}/admin": "Admin access",
            f"https://{settings.AZURE_B2C_TENANT_NAME}.onmicrosoft.com/{settings.AZURE_CLIENT_ID}/read": "Read access"
        }
    )


# Create the authentication scheme based on configuration
azure_scheme = create_azure_auth_scheme() or create_azure_b2c_auth_scheme()


def user_has_admin_access(user: User) -> bool:
    """Check if user has admin access based on roles/scopes"""
    if not user:
        return False
    
    # Check for admin scope
    admin_scopes = [
        f"api://{settings.AZURE_CLIENT_ID}/admin",
        f"https://{settings.AZURE_B2C_TENANT_NAME}.onmicrosoft.com/{settings.AZURE_CLIENT_ID}/admin"
    ]
    
    user_scopes = getattr(user, 'scp', '').split() if hasattr(user, 'scp') else []
    user_roles = getattr(user, 'roles', []) if hasattr(user, 'roles') else []
    
    # Check scopes
    for scope in admin_scopes:
        if scope in user_scopes:
            return True
    
    # Check roles (if configured in Azure AD)
    if 'Admin' in user_roles or 'Portfolio.Admin' in user_roles:
        return True
    
    return False