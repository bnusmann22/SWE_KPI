"""
Base database configuration and model registry.
All models should inherit from this Base class.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all models."""
    __allow_unmapped__ = True
