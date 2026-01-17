"""Student schemas for API requests/responses."""

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.common import TimestampSchema


class StudentBase(BaseModel):
    """Base student schema with common fields."""

    matric_number: str = Field(..., min_length=5, description="Matric/Student number")
    first_name: str = Field(..., min_length=2, description="First name")
    last_name: str = Field(..., min_length=2, description="Last name")
    email: str = Field(..., description="Email address")
    level: int = Field(..., ge=100, le=400, description="Student level (100-400)")
    department_id: int = Field(..., description="Department ID")
    github_username: Optional[str] = Field(None, description="GitHub username")


class StudentCreate(StudentBase):
    """Schema for creating a new student."""

    pass


class StudentUpdate(BaseModel):
    """Schema for updating a student."""

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    level: Optional[int] = None
    github_username: Optional[str] = None
    is_active: Optional[bool] = None


class StudentResponse(StudentBase, TimestampSchema):
    """Student response schema."""

    id: int
    is_active: bool

    class Config:
        from_attributes = True


class StudentProjectResponse(BaseModel):
    """Student project response."""

    id: int
    student_id: int
    project_name: str
    github_url: Optional[str] = None
    is_deployed: bool
    deployment_url: Optional[str] = None
    technologies_used: Optional[list[str]] = None
    project_quality_score: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True
