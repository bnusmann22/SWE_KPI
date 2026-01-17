"""Student feedback model."""

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class StudentFeedback(BaseModel):
    """Student feedback on courses and teaching effectiveness."""

    __tablename__ = "student_feedback"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    academic_session_id = Column(Integer, ForeignKey("academic_sessions.id"), nullable=False)
    rating = Column(Integer, nullable=False)  # 1-5 scale
    comments = Column(Text, nullable=True)
    is_anonymous = Column(Integer, default=1, nullable=False)  # 1 for anonymous, 0 for identified

    # Relationships
    course = relationship("Course", back_populates="feedback_records")
    student = relationship("Student", back_populates="feedback")
    academic_session = relationship("AcademicSession")

    def __repr__(self) -> str:
        return f"<StudentFeedback(id={self.id}, course_id={self.course_id}, rating={self.rating})>"
