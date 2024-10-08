import datetime
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, LargeBinary, DateTime


class UserModel(Base):
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[int]
    username: Mapped[str] = mapped_column(String(25), unique=True)
    email_address: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    active: Mapped[bool] = mapped_column(default=True)
    paid: Mapped[bool] = mapped_column(default=False)

    create_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
    )
    update_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
        onupdate=lambda: datetime.datetime.now(datetime.timezone.utc),
    )
