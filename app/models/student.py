"""Student and StudentProject models."""

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Student(BaseModel):
    """Student model representing a department student."""

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    matric_number = Column(String(50), unique=True, nullable=False, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    level = Column(Integer, nullable=False)  # 100, 200, 300, 400 (year level)
    github_username = Column(String(100), nullable=True, unique=True)
    is_active = Column(Boolean, default=True, nullable=False)

    # Relationships
    department = relationship("Department", back_populates="students")
    projects = relationship("StudentProject", back_populates="student", cascade="all, delete-orphan")
    internships = relationship("InternshipRecord", back_populates="student", cascade="all, delete-orphan")
    feedback = relationship("StudentFeedback", back_populates="student", cascade="all, delete-orphan")
    event_participations = relationship("EventParticipant", back_populates="student", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Student(id={self.id}, matric_number={self.matric_number}, name={self.first_name} {self.last_name})>"


class StudentProject(BaseModel):
    """Student project model tracking capstone/final projects."""

    __tablename__ = "student_projects"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    project_name = Column(String(255), nullable=False)
    project_description = Column(String(1000), nullable=True)
    github_url = Column(String(500), nullable=True)
    is_deployed = Column(Boolean, default=False, nullable=False)
    deployment_url = Column(String(500), nullable=True)
    technologies_used = Column(JSON, default=list, nullable=True)
    academic_session_id = Column(Integer, ForeignKey("academic_sessions.id"), nullable=False)
    project_quality_score = Column(Integer, nullable=True)  # 0-100

    # Relationships
    student = relationship("Student", back_populates="projects")
    academic_session = relationship("AcademicSession")

    def __repr__(self) -> str:
        return f"<StudentProject(id={self.id}, project_name={self.project_name})>"
