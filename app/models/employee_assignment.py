
from datetime import date, datetime

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    text,
    CheckConstraint
)
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class EmployeeAssignment(Base):
    __tablename__ = "employee_assignments"

    __table_args__ = (
        CheckConstraint(
            "effective_to IS NULL OR effective_to >= effective_from",
            name="ck_assignments_effective_dates"
        ),
    )

    # Primary Key
    assignment_id: Mapped[str] = mapped_column(
        String(12),
        primary_key=True
    )

    # Employee Foreign Key
    employee_id: Mapped[str] = mapped_column(
        String(10),
        ForeignKey("employees.employee_id"),
        nullable=False
    )

    # Assignment period
    effective_from: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    effective_to: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    # Department Foreign Key
    department_id: Mapped[str] = mapped_column(
        String(10),
        ForeignKey("departments.department_id"),
        nullable=False
    )

    # Role Foreign Key
    role_id: Mapped[str] = mapped_column(
        String(10),
        ForeignKey("roles.role_id"),
        nullable=False
    )

    job_level: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    # Manager Foreign Key
    manager_id: Mapped[str | None] = mapped_column(
        String(10),
        ForeignKey("employees.employee_id"),
        nullable=True
    )

    change_reason: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Audit fields
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        server_default=text("true"),
        nullable=False
    )
