"""Tests for security utilities."""

import pytest

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    decode_token,
)


class TestPasswordHashing:
    """Tests for password hashing and verification."""

    def test_hash_password(self):
        """Test password hashing."""
        password = "test_password_123"
        hashed = hash_password(password)

        assert hashed != password
        assert len(hashed) > len(password)

    def test_verify_password(self):
        """Test password verification."""
        password = "test_password_123"
        hashed = hash_password(password)

        assert verify_password(password, hashed)
        assert not verify_password("wrong_password", hashed)


class TestTokenGeneration:
    """Tests for JWT token generation and decoding."""

    def test_create_access_token(self):
        """Test access token creation."""
        token = create_access_token(subject="user_123")

        assert isinstance(token, str)
        assert len(token) > 0

    def test_decode_token(self):
        """Test token decoding."""
        subject = "user_123"
        token = create_access_token(subject=subject)

        decoded = decode_token(token)
        assert decoded is not None
        assert decoded["sub"] == subject

    def test_decode_invalid_token(self):
        """Test decoding invalid token."""
        decoded = decode_token("invalid_token_string")
        assert decoded is None
