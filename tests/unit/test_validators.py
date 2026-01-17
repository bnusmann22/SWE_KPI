"""Tests for validation utilities."""

import pytest

from app.utils.validators import (
    validate_email,
    validate_github_username,
    validate_matric_number,
)


class TestEmailValidation:
    """Tests for email validation."""

    def test_valid_email(self):
        """Test valid email addresses."""
        assert validate_email("user@example.com")
        assert validate_email("john.doe+tag@university.edu.ng")

    def test_invalid_email(self):
        """Test invalid email addresses."""
        assert not validate_email("invalid.email")
        assert not validate_email("@example.com")
        assert not validate_email("user@")


class TestGithubUsernameValidation:
    """Tests for GitHub username validation."""

    def test_valid_github_username(self):
        """Test valid GitHub usernames."""
        assert validate_github_username("johndoe")
        assert validate_github_username("john-doe")
        assert validate_github_username("j")

    def test_invalid_github_username(self):
        """Test invalid GitHub usernames."""
        assert not validate_github_username("john_doe")  # Underscore not allowed
        assert not validate_github_username("john doe")  # Space not allowed
        assert not validate_github_username("a" * 40)  # Too long


class TestMatricNumberValidation:
    """Tests for matric number validation."""

    def test_valid_matric_numbers(self):
        """Test valid matric numbers."""
        assert validate_matric_number("CSC/2021/001")
        assert validate_matric_number("SE/2020/100")
        assert validate_matric_number("PHYS/2022/050")

    def test_invalid_matric_numbers(self):
        """Test invalid matric numbers."""
        assert not validate_matric_number("CSC-2021-001")
        assert not validate_matric_number("2021/CSC/001")
        assert not validate_matric_number("CSC/21/001")  # Year too short
