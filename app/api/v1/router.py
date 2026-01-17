"""
Main router for API v1.
Includes all endpoint routers.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import health, auth, students

api_router = APIRouter(prefix="/api/v1")

# Include routers
api_router.include_router(health.router, tags=["health"])
api_router.include_router(auth.router, tags=["authentication"])
api_router.include_router(students.router, tags=["students"])
