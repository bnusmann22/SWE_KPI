"""
Database initialization script.
Creates all tables and sets up initial database schema.

Usage:
    python scripts/init_db.py
"""

import logging
from sqlalchemy import create_engine

from app.core.config import settings
from app.db.base import Base
from app.models import *  # noqa: F401, F403

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db() -> None:
    """Initialize database by creating all tables."""
    logger.info("Connecting to database...")
    engine = create_engine(settings.DATABASE_URL)

    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)

    logger.info("Database initialization complete!")


if __name__ == "__main__":
    init_db()
