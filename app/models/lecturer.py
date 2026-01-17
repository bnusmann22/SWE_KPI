"""Lecturer model."""

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Lecturer(BaseModel):
    """Lecturer/Instructor model."""

    __tablename__ = "lecturers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    uses_lms = Column(Boolean, default=False, nullable=False)
    training_sessions_attended = Column(Integer, default=0, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # Relationships
    department = relationship("Department", back_populates="lecturers")
    courses = relationship("Course", back_populates="lecturer")

    def __repr__(self) -> str:
        return f"<Lecturer(id={self.id}, name={self.name}, email={self.email})>"
