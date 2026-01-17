"""Data formatting utilities."""

from datetime import datetime
from typing import Any, Dict


def format_date(date_obj: datetime, format_str: str = "%Y-%m-%d") -> str:
    """
    Format datetime object to string.

    Args:
        date_obj: Datetime object
        format_str: Format string

    Returns:
        Formatted date string
    """
    if isinstance(date_obj, datetime):
        return date_obj.strftime(format_str)
    return str(date_obj)


def format_percentage(value: float, decimal_places: int = 2) -> str:
    """
    Format value as percentage.

    Args:
        value: Numeric value
        decimal_places: Number of decimal places

    Returns:
        Formatted percentage string
    """
    return f"{value:.{decimal_places}f}%"


def format_currency(amount: float, currency: str = "NGN") -> str:
    """
    Format amount as currency.

    Args:
        amount: Numeric amount
        currency: Currency code

    Returns:
        Formatted currency string
    """
    return f"{currency} {amount:,.2f}"
