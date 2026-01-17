"""Base model classes with common fields."""

from datetime import datetime
from typing import Any

from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import declared_attr

from app.db.base import Base


class TimestampMixin:
    """Mixin that adds created_at and updated_at timestamps."""

    @declared_attr
    def created_at(cls) -> Any:
        """Timestamp when record was created."""
        return Column(DateTime, default=func.now(), nullable=False)

    @declared_attr
    def updated_at(cls) -> Any:
        """Timestamp when record was last updated."""
        return Column(
            DateTime,
            default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )


class BaseModel(Base, TimestampMixin):
    """Abstract base model with common fields."""

    __abstract__ = True
