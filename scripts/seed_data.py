"""
Database seeding script.
Populates database with sample data for development and testing.

Usage:
    python scripts/seed_data.py
"""

import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.models import (
    Department,
    AcademicSession,
    Course,
    Lecturer,
    Student,
    User,
)
from app.core.security import hash_password

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def seed_database() -> None:
    """Seed the database with sample data."""
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        logger.info("Seeding database with sample data...")

        # Check if data already exists
        if db.query(Department).first():
            logger.info("Database already contains data. Skipping seed.")
            return

        # Create sample user
        logger.info("Creating sample user...")
        user = User(
            email="admin@kpisystem.edu.ng",
            username="admin",
            hashed_password=hash_password("admin123"),
            full_name="System Administrator",
            is_active=True,
            is_superuser=True,
        )
        db.add(user)

        # Create departments
        logger.info("Creating departments...")
        cs_dept = Department(
            name="Computer Science",
            code="CS",
            faculty="Engineering",
            head_of_department="Prof. Dr. John Smith",
        )
        se_dept = Department(
            name="Software Engineering",
            code="SE",
            faculty="Engineering",
            head_of_department="Prof. Dr. Jane Doe",
        )
        db.add_all([cs_dept, se_dept])
        db.flush()

        # Create academic sessions
        logger.info("Creating academic sessions...")
        session_2023_1 = AcademicSession(
            session_name="2023/2024",
            start_date="2023-09-01",
            end_date="2024-02-28",
            semester=1,
            is_active=1,
        )
        session_2023_2 = AcademicSession(
            session_name="2023/2024",
            start_date="2024-03-01",
            end_date="2024-08-31",
            semester=2,
            is_active=0,
        )
        db.add_all([session_2023_1, session_2023_2])
        db.flush()

        # Create lecturers
        logger.info("Creating lecturers...")
        lecturer1 = Lecturer(
            name="Dr. Alice Johnson",
            email="alice.johnson@university.edu",
            department_id=cs_dept.id,
            uses_lms=True,
            training_sessions_attended=5,
            is_active=True,
        )
        lecturer2 = Lecturer(
            name="Prof. Bob Williams",
            email="bob.williams@university.edu",
            department_id=se_dept.id,
            uses_lms=True,
            training_sessions_attended=3,
            is_active=True,
        )
        db.add_all([lecturer1, lecturer2])
        db.flush()

        # Create courses
        logger.info("Creating courses...")
        course1 = Course(
            course_code="CS101",
            course_title="Introduction to Programming",
            department_id=cs_dept.id,
            lecturer_id=lecturer1.id,
            credits=3,
            has_practical_project=True,
            practical_sessions_count=15,
            theoretical_sessions_count=30,
            tools_used=["Python", "Git", "VS Code"],
        )
        course2 = Course(
            course_code="SE201",
            course_title="Software Design Patterns",
            department_id=se_dept.id,
            lecturer_id=lecturer2.id,
            credits=4,
            has_practical_project=True,
            practical_sessions_count=20,
            theoretical_sessions_count=25,
            tools_used=["Java", "UML", "Design Patterns"],
        )
        db.add_all([course1, course2])
        db.flush()

        # Create students
        logger.info("Creating students...")
        students = [
            Student(
                matric_number="CSC/2021/001",
                first_name="John",
                last_name="Adeyemi",
                email="john.adeyemi@student.edu",
                department_id=cs_dept.id,
                level=300,
                github_username="johnadeyemi",
                is_active=True,
            ),
            Student(
                matric_number="CSC/2021/002",
                first_name="Mary",
                last_name="Okonkwo",
                email="mary.okonkwo@student.edu",
                department_id=cs_dept.id,
                level=300,
                github_username="maryokonkwo",
                is_active=True,
            ),
            Student(
                matric_number="SE/2021/001",
                first_name="David",
                last_name="Okafor",
                email="david.okafor@student.edu",
                department_id=se_dept.id,
                level=300,
                github_username="davidokafor",
                is_active=True,
            ),
            Student(
                matric_number="SE/2021/002",
                first_name="Zainab",
                last_name="Hassan",
                email="zainab.hassan@student.edu",
                department_id=se_dept.id,
                level=300,
                github_username="zainahassan",
                is_active=True,
            ),
        ]
        db.add_all(students)

        # Commit all changes
        db.commit()
        logger.info("Database seeding completed successfully!")

    except Exception as e:
        logger.error(f"Error seeding database: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
