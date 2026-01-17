"""KPI snapshot and calculation models."""

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class KPISnapshot(BaseModel):
    """Snapshot of calculated KPI values for a session."""

    __tablename__ = "kpi_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    academic_session_id = Column(Integer, ForeignKey("academic_sessions.id"), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    pillar_name = Column(String(100), nullable=False)  # academic_quality, employability, etc.
    metric_name = Column(String(255), nullable=False)  # Specific metric name
    calculated_value = Column(Float, nullable=False)  # Actual calculated value
    target_value = Column(Float, nullable=False)  # Target value for comparison
    percentage_achieved = Column(Float, nullable=False)  # (calculated/target) * 100
    status = Column(String(50), nullable=False)  # "exceeds", "meets", "below"

    # Relationships
    academic_session = relationship("AcademicSession")
    department = relationship("Department", back_populates="kpi_snapshots")

    def __repr__(self) -> str:
        return f"<KPISnapshot(id={self.id}, pillar={self.pillar_name}, metric={self.metric_name})>"
