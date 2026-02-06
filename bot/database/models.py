import logging
from contextlib import asynccontextmanager

from sqlalchemy import BigInteger
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

logger = logging.getLogger(__name__)

engine = create_async_engine(
    url="sqlite+aiosqlite:////app/data/db.sqlite3", #///db.sqlite3 для локальной разработки
    echo=True,
)

async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class User(Base):
    """Модель пользователя."""

    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)  # id в TG


class Blacklist(Base):
    """Модель черного списка."""

    __tablename__ = "blacklist"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    owner_id: Mapped[int] = mapped_column(BigInteger)
    blocked_user_id: Mapped[int] = mapped_column(BigInteger)


@asynccontextmanager
async def session_scope(*, commit: bool = False):
    """
    Контекстный менеджер для сессий с БД.
    Если commit=True, то при выходе из контекста будет выполнен коммит.
    """
    async with async_session() as session:
        try:
            yield session
            if commit:
                await session.commit()
        except Exception:
            await session.rollback()
            logger.exception("DB transaction failed")
            raise


async def async_main():
    """Создание всех таблиц в БД при старте бота."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
