"""Course and CourseOutline models."""

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Course(BaseModel):
    """Course model representing an academic course."""

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_code = Column(String(50), nullable=False, unique=True, index=True)
    course_title = Column(String(255), nullable=False, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    lecturer_id = Column(Integer, ForeignKey("lecturers.id"), nullable=True)
    credits = Column(Integer, default=3, nullable=False)
    has_practical_project = Column(Boolean, default=False, nullable=False)
    practical_sessions_count = Column(Integer, default=0, nullable=False)
    theoretical_sessions_count = Column(Integer, default=0, nullable=False)
    tools_used = Column(JSON, default=list, nullable=True)  # Array of tools/technologies

    # Relationships
    department = relationship("Department", back_populates="courses")
    lecturer = relationship("Lecturer", back_populates="courses")
    course_outlines = relationship("CourseOutline", back_populates="course", cascade="all, delete-orphan")
    feedback_records = relationship("StudentFeedback", back_populates="course", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Course(id={self.id}, course_code={self.course_code}, title={self.course_title})>"


class CourseOutline(BaseModel):
    """Course outline tracking model."""

    __tablename__ = "course_outlines"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    academic_session_id = Column(Integer, ForeignKey("academic_sessions.id"), nullable=False)
    outline_content = Column(String(1000), nullable=True)
    is_current = Column(Boolean, default=True, nullable=False)

    # Relationships
    course = relationship("Course", back_populates="course_outlines")
    academic_session = relationship("AcademicSession")

    def __repr__(self) -> str:
        return f"<CourseOutline(id={self.id}, course_id={self.course_id})>"
