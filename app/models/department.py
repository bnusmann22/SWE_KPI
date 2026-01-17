"""Department model."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Department(BaseModel):
    """Department model representing an academic department."""

    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)
    faculty = Column(String(255), nullable=False)
    head_of_department = Column(String(255), nullable=True)

    # Relationships
    courses = relationship("Course", back_populates="department", cascade="all, delete-orphan")
    students = relationship("Student", back_populates="department", cascade="all, delete-orphan")
    lecturers = relationship("Lecturer", back_populates="department", cascade="all, delete-orphan")
    kpi_snapshots = relationship("KPISnapshot", back_populates="department", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Department(id={self.id}, name={self.name}, code={self.code})>"


class AcademicSession(BaseModel):
    """Academic session model for tracking semesters."""

    __tablename__ = "academic_sessions"

    id = Column(Integer, primary_key=True, index=True)
    session_name = Column(String(50), nullable=False, unique=True)  # e.g., "2023/2024"
    start_date = Column(String(10), nullable=False)  # Format: YYYY-MM-DD
    end_date = Column(String(10), nullable=False)
    semester = Column(Integer, nullable=False)  # 1 or 2
    is_active = Column(Integer, default=0, nullable=False)  # 1 for active, 0 for inactive

    def __repr__(self) -> str:
        return f"<AcademicSession(id={self.id}, session_name={self.session_name}, semester={self.semester})>"
