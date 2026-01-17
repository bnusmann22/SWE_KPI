"""Database models package - import all models here."""

from app.models.base import BaseModel, TimestampMixin
from app.models.user import User
from app.models.department import Department, AcademicSession
from app.models.course import Course, CourseOutline
from app.models.student import Student, StudentProject
from app.models.lecturer import Lecturer
from app.models.internship import InternshipRecord
from app.models.feedback import StudentFeedback
from app.models.event import Event, EventParticipant
from app.models.kpi import KPISnapshot

__all__ = [
    "BaseModel",
    "TimestampMixin",
    "User",
    "Department",
    "AcademicSession",
    "Course",
    "CourseOutline",
    "Student",
    "StudentProject",
    "Lecturer",
    "InternshipRecord",
    "StudentFeedback",
    "Event",
    "EventParticipant",
    "KPISnapshot",
]
