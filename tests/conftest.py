"""
Pytest configuration and shared fixtures for all tests.
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool

from app.db.base import Base


@pytest.fixture(scope="session")
def test_database_url():
    """Provide test database URL."""
    return "sqlite:///:memory:"


@pytest.fixture(scope="session")
def engine(test_database_url):
    """Create test database engine."""
    engine = create_engine(
        test_database_url,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    yield engine
    engine.dispose()


@pytest.fixture(scope="function")
def db_session(engine):
    """Create test database session."""
    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def mock_settings(monkeypatch):
    """Provide mock settings for tests."""
    test_settings = {
        "APP_NAME": "KPI System Test",
        "ENVIRONMENT": "test",
        "DEBUG": True,
        "SECRET_KEY": "test-secret-key",
        "JWT_SECRET_KEY": "test-jwt-secret",
        "DATABASE_URL": "sqlite:///:memory:",
    }

    for key, value in test_settings.items():
        monkeypatch.setenv(key, str(value))
