"""Application configuration"""
import os
from typing import List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Application settings"""
    
    # Azure AD Configuration
    AZURE_TENANT_ID: str = os.getenv("AZURE_TENANT_ID", "")
    AZURE_CLIENT_ID: str = os.getenv("AZURE_CLIENT_ID", "")
    AZURE_CLIENT_SECRET: str = os.getenv("AZURE_CLIENT_SECRET", "")  # Optional with managed identity
    USE_MANAGED_IDENTITY: bool = os.getenv("USE_MANAGED_IDENTITY", "false").lower() == "true"
    
    # Azure AD B2C Configuration (if using B2C instead of regular AD)
    AZURE_B2C_TENANT_NAME: str = os.getenv("AZURE_B2C_TENANT_NAME", "")  # e.g., "yourtenant"
    AZURE_B2C_POLICY_NAME: str = os.getenv("AZURE_B2C_POLICY_NAME", "B2C_1_signupsignin")
    
    # CORS Configuration
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",  # Local development
        "http://localhost:5173",  # Vite dev server
        # Add your production frontend URL here
        # "https://your-frontend-domain.com"
    ]
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./portfolio.db")
    
    @property
    def is_azure_ad_configured(self) -> bool:
        """Check if Azure AD is properly configured"""
        return bool(self.AZURE_TENANT_ID and self.AZURE_CLIENT_ID)
    
    @property
    def is_azure_b2c_configured(self) -> bool:
        """Check if Azure AD B2C is properly configured"""
        return bool(self.AZURE_B2C_TENANT_NAME and self.AZURE_CLIENT_ID)


settings = Settings()
