"""KPI schemas for API requests/responses."""

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class KPIMetric(BaseModel):
    """Individual KPI metric."""

    metric_name: str = Field(..., description="Name of the metric")
    calculated_value: float = Field(..., description="Calculated value")
    target_value: float = Field(..., description="Target value")
    percentage_achieved: float = Field(..., description="Percentage of target achieved")
    status: str = Field(..., description="Status: exceeds, meets, or below")


class KPIPillar(BaseModel):
    """KPI pillar containing multiple metrics."""

    pillar_name: str = Field(..., description="Name of the pillar")
    metrics: list[KPIMetric] = Field(..., description="List of metrics in this pillar")


class KPISnapshot(BaseModel):
    """Complete KPI snapshot for a session."""

    academic_session_id: int
    department_id: int
    timestamp: datetime
    pillars: dict[str, KPIPillar] = Field(..., description="Dictionary of KPI pillars")
    overall_score: float = Field(..., description="Overall department KPI score")

    class Config:
        from_attributes = True
