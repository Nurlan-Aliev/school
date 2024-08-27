from asyncio import current_task
from config import setting
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr,
)
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


class DataBaseHelper:
    def __init__(self, url, echo):
        self.async_engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.async_session_factory = async_sessionmaker(
            self.async_engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    def get_scoped_session(self):

        return async_scoped_session(
            self.async_session_factory,
            scopefunc=current_task,
        )

    def scope_session_dependency(self):
        session = self.get_scoped_session()
        yield session
        session.close()


db_helper = DataBaseHelper(
    setting.db_connect,
    setting.DEBUG,
)