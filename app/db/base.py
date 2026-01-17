"""
Base database configuration and model registry.
All models should inherit from this Base class.
"""

from sqlalchemy.orm import declarative_base

Base = declarative_base()
