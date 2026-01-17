"""Internship and work experience models."""

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class InternshipRecord(BaseModel):
    """Internship/SIWES participation record."""

    __tablename__ = "internship_records"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    company_name = Column(String(255), nullable=False)
    company_location = Column(String(255), nullable=True)
    internship_type = Column(String(50), nullable=False)  # "Internship", "SIWES", "Co-op"
    start_date = Column(String(10), nullable=False)  # Format: YYYY-MM-DD
    end_date = Column(String(10), nullable=False)
    academic_session_id = Column(Integer, ForeignKey("academic_sessions.id"), nullable=False)
    duration_weeks = Column(Integer, nullable=True)
    supervisor_name = Column(String(255), nullable=True)
    performance_rating = Column(Integer, nullable=True)  # 1-5 scale

    # Relationships
    student = relationship("Student", back_populates="internships")
    academic_session = relationship("AcademicSession")

    def __repr__(self) -> str:
        return f"<InternshipRecord(id={self.id}, student_id={self.student_id}, company={self.company_name})>"
