
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    func,
    text,
    CheckConstraint,
    Index,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Employee(Base):
    __tablename__ = "employees"

    __table_args__ = (
        UniqueConstraint(
            "work_email",
            name="uq_employees_work_email"
        ),

        CheckConstraint(
            "exit_date IS NULL OR exit_date >= hire_date",
            name="ck_employees_exit_date"
        ),

        Index(
            "ix_employees_department_id",
            "department_id"
        ),

        Index(
            "ix_employees_manager_id",
            "manager_id"
        ),

        Index(
            "ix_employees_full_name",
            "full_name"
        ),

        Index(
            "ix_employees_employment_status",
            "employment_status"
        ),
    )

    # Primary Key
    employee_id: Mapped[str] = mapped_column(
        String(10),
        primary_key=True
    )

    # Personal details
    first_name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
    last_name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
    full_name: Mapped[str] = mapped_column(
        String(200), nullable=False
    )
    work_email: Mapped[str] = mapped_column(
        String(254), nullable=False
    )
    gender: Mapped[str] = mapped_column(
        String(20), nullable=False
    )
    date_of_birth: Mapped[date] = mapped_column(
        Date, nullable=False
    )

    # Employment details
    hire_date: Mapped[date] = mapped_column(
        Date, nullable=False
    )
    exit_date: Mapped[date | None] = mapped_column(
        Date, nullable=True
    )
    employment_status: Mapped[str] = mapped_column(
        String(30), nullable=False
    )
    employment_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )

    # Foreign Keys
    department_id: Mapped[str] = mapped_column(
        String(10),
        ForeignKey("departments.department_id"),
        nullable=False
    )
    role_id: Mapped[str] = mapped_column(
        String(10),
        ForeignKey("roles.role_id"),
        nullable=False
    )
    manager_id: Mapped[str | None] = mapped_column(
        String(10),
        ForeignKey("employees.employee_id"),
        nullable=True
    )

    # Workplace information
    work_location: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
    work_mode: Mapped[str] = mapped_column(
        String(20), nullable=False
    )
    highest_education: Mapped[str | None] = mapped_column(
        String(150), nullable=True
    )

    # Experience and commute
    prior_experience_years: Mapped[Decimal] = mapped_column(
        Numeric(5, 1), nullable=False
    )
    career_gap_months: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    commute_distance_km: Mapped[Decimal] = mapped_column(
        Numeric(6, 1), nullable=False
    )

    # Statutory information
    pf_applicable: Mapped[str] = mapped_column(
        String(1), nullable=False
    )
    esi_applicable: Mapped[str] = mapped_column(
        String(1), nullable=False
    )
    notice_period_days: Mapped[int] = mapped_column(
        Integer, nullable=False
    )

    # Exit information
    resignation_date: Mapped[date | None] = mapped_column(
        Date, nullable=True
    )
    exit_type: Mapped[str | None] = mapped_column(
        String(50), nullable=True
    )
    exit_reason: Mapped[str | None] = mapped_column(
        String(255), nullable=True
    )

    # Audit information
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
