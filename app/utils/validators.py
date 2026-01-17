"""Data validation utilities."""

from typing import Any
from pydantic import ValidationError


def validate_email(email: str) -> bool:
    """
    Validate email format.

    Args:
        email: Email address to validate

    Returns:
        True if valid, False otherwise
    """
    import re
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_github_username(username: str) -> bool:
    """
    Validate GitHub username format.

    Args:
        username: GitHub username

    Returns:
        True if valid, False otherwise
    """
    import re
    # GitHub usernames are alphanumeric and hyphens, 1-39 characters
    pattern = r"^[a-zA-Z0-9-]{1,39}$"
    return bool(re.match(pattern, username))


def validate_matric_number(matric: str) -> bool:
    """
    Validate matric number format (e.g., CSC/2021/001).

    Args:
        matric: Matric number

    Returns:
        True if valid, False otherwise
    """
    import re
    pattern = r"^[A-Z]{2,4}/\d{4}/\d{3,4}$"
    return bool(re.match(pattern, matric))
