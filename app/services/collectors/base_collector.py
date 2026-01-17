"""
Base collector class for all data collectors.
All data source integrations should inherit from this.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from sqlalchemy.orm import Session


class BaseCollector(ABC):
    """Abstract base class for data collectors."""

    def __init__(self, session: Session):
        """
        Initialize collector.

        Args:
            session: Database session
        """
        self.session = session

    @abstractmethod
    def collect(self, **kwargs) -> List[Dict[str, Any]]:
        """
        Collect data from source.

        Returns:
            List of collected data items
        """
        pass

    @abstractmethod
    def validate(self, data: Dict[str, Any]) -> bool:
        """
        Validate collected data.

        Args:
            data: Data item to validate

        Returns:
            True if valid, False otherwise
        """
        pass
