"""Course schemas for API requests/responses."""

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.common import TimestampSchema


class CourseBase(BaseModel):
    """Base course schema."""

    course_code: str = Field(..., min_length=3, description="Course code")
    course_title: str = Field(..., min_length=3, description="Course title")
    department_id: int = Field(..., description="Department ID")
    credits: int = Field(default=3, ge=1, le=6, description="Credit hours")
    has_practical_project: bool = Field(default=False)
    practical_sessions_count: int = Field(default=0, ge=0)
    theoretical_sessions_count: int = Field(default=0, ge=0)
    tools_used: Optional[list[str]] = Field(None, description="Tools/technologies used")


class CourseCreate(CourseBase):
    """Schema for creating a course."""

    pass


class CourseUpdate(BaseModel):
    """Schema for updating a course."""

    course_title: Optional[str] = None
    credits: Optional[int] = None
    has_practical_project: Optional[bool] = None
    practical_sessions_count: Optional[int] = None
    theoretical_sessions_count: Optional[int] = None
    tools_used: Optional[list[str]] = None


class CourseResponse(CourseBase, TimestampSchema):
    """Course response schema."""

    id: int
    lecturer_id: Optional[int] = None

    class Config:
        from_attributes = True
