
from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Role(Base):
    __tablename__ = "roles"

    role_id: Mapped[str] = mapped_column(
        String(10),
        primary_key=True
    )

    department_id: Mapped[str] = mapped_column(
        String(10),
        ForeignKey("departments.department_id"),
        nullable=False
    )

    role_title: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    level: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    grade: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    band_min_annual: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    band_mid_annual: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    band_max_annual: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    overtime_eligible: Mapped[str] = mapped_column(
        String(1),
        nullable=False
    )

    band_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

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
