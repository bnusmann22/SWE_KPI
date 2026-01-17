"""
Base calculator class for all KPI calculators.
All specific KPI calculators should inherit from this.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from sqlalchemy.orm import Session


class BaseCalculator(ABC):
    """Abstract base class for KPI calculators."""

    def __init__(self, session: Session):
        """
        Initialize calculator.

        Args:
            session: Database session
        """
        self.session = session
        self.metrics = {}

    @abstractmethod
    def calculate(self, department_id: int, session_id: int) -> Dict[str, Any]:
        """
        Calculate KPI metrics.

        Args:
            department_id: Department ID
            session_id: Academic session ID

        Returns:
            Dictionary of calculated metrics
        """
        pass

    def _get_percentage(self, actual: float, target: float) -> float:
        """
        Calculate percentage achievement.

        Args:
            actual: Actual value
            target: Target value

        Returns:
            Percentage (0-100+)
        """
        if target == 0:
            return 0.0
        return (actual / target) * 100

    def _get_status(self, percentage: float, threshold: float = 100) -> str:
        """
        Determine status based on percentage.

        Args:
            percentage: Percentage achieved
            threshold: Threshold percentage (default 100%)

        Returns:
            Status: "exceeds", "meets", or "below"
        """
        if percentage >= 110:
            return "exceeds"
        elif percentage >= threshold:
            return "meets"
        else:
            return "below"
