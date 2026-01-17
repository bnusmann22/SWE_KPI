"""User CRUD operations."""

from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User


class CRUDUser(CRUDBase[User, dict, dict]):
    """CRUD operations for User model."""

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        """Get user by email."""
        return db.query(self.model).filter(self.model.email == email).first()

    def get_by_username(self, db: Session, username: str) -> Optional[User]:
        """Get user by username."""
        return db.query(self.model).filter(self.model.username == username).first()


# Create CRUD instance
crud_user = CRUDUser(User)
