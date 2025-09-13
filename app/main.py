"""FastAPI application"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from app.db.database import engine
from app.routers import profile_router
from app.auth.azure_ad import azure_scheme
from app.config import settings


# noinspection PyUnusedLocal
@asynccontextmanager
async def lifespan(app_instance: FastAPI):
    """Create database tables on startup"""
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(
    title="Tom Boone Portfolio Backend", 
    description="Backend API for Tom Boone's portfolio website",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Configure Azure AD integration if available
if azure_scheme:
    app.include_router(azure_scheme.router, prefix="/auth", tags=["auth"])

# Include routers
app.include_router(profile_router, prefix="/api/v1")


@app.get("/")
def root():
    """Health check endpoint"""
    return {"message": "Tom Boone Portfolio Backend API"}
