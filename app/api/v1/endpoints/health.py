"""Health check endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "message": "API is running",
    }


@router.get("/info")
async def api_info():
    """Get API information."""
    return {
        "name": "KPI System API",
        "version": "1.0.0",
        "status": "operational",
    }
