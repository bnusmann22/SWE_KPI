"""Student CRUD operations."""

from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.student import Student


class CRUDStudent(CRUDBase[Student, dict, dict]):
    """CRUD operations for Student model."""

    def get_by_matric(self, db: Session, matric_number: str) -> Optional[Student]:
        """Get student by matric number."""
        return db.query(self.model).filter(
            self.model.matric_number == matric_number
        ).first()

    def get_by_email(self, db: Session, email: str) -> Optional[Student]:
        """Get student by email."""
        return db.query(self.model).filter(self.model.email == email).first()

    def get_by_github(self, db: Session, github_username: str) -> Optional[Student]:
        """Get student by GitHub username."""
        return db.query(self.model).filter(
            self.model.github_username == github_username
        ).first()


# Create CRUD instance
crud_student = CRUDStudent(Student)
