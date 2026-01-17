"""Event and participation models."""

from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Event(BaseModel):
    """Event model (workshops, hackathons, seminars, guest sessions)."""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String(255), nullable=False)
    event_type = Column(String(50), nullable=False)  # workshop, hackathon, seminar, guest_session
    organizer = Column(String(255), nullable=False)
    event_date = Column(String(10), nullable=False)  # Format: YYYY-MM-DD
    academic_session_id = Column(Integer, ForeignKey("academic_sessions.id"), nullable=False)
    description = Column(String(1000), nullable=True)
    location = Column(String(255), nullable=True)

    # Relationships
    participants = relationship("EventParticipant", back_populates="event", cascade="all, delete-orphan")
    academic_session = relationship("AcademicSession")

    def __repr__(self) -> str:
        return f"<Event(id={self.id}, name={self.event_name}, type={self.event_type})>"


class EventParticipant(BaseModel):
    """Event participation record."""

    __tablename__ = "event_participants"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    participation_date = Column(String(10), nullable=False)

    # Relationships
    event = relationship("Event", back_populates="participants")
    student = relationship("Student", back_populates="event_participations")

    def __repr__(self) -> str:
        return f"<EventParticipant(id={self.id}, event_id={self.event_id}, student_id={self.student_id})>"
