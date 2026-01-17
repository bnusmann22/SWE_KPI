"""
Create an admin user script.

Usage:
    python scripts/create_admin.py
"""

import logging
from getpass import getpass
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.models.user import User
from app.core.security import hash_password

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_admin_user() -> None:
    """Interactively create an admin user."""
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        print("Create Admin User")
        print("=" * 50)

        email = input("Enter admin email: ").strip()
        username = input("Enter admin username: ").strip()
        full_name = input("Enter full name: ").strip()
        password = getpass("Enter password: ")
        password_confirm = getpass("Confirm password: ")

        if password != password_confirm:
            logger.error("Passwords do not match!")
            return

        if len(password) < 8:
            logger.error("Password must be at least 8 characters long!")
            return

        # Check if user exists
        existing = db.query(User).filter(
            (User.email == email) | (User.username == username)
        ).first()

        if existing:
            logger.error("User with this email or username already exists!")
            return

        # Create user
        user = User(
            email=email,
            username=username,
            full_name=full_name,
            hashed_password=hash_password(password),
            is_active=True,
            is_superuser=True,
        )
        db.add(user)
        db.commit()

        logger.info(f"Admin user '{username}' created successfully!")

    except Exception as e:
        logger.error(f"Error creating admin user: {str(e)}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    create_admin_user()
