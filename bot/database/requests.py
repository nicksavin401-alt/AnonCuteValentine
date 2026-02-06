from __future__ import annotations
from sqlalchemy import delete, select
from database.models import Blacklist, User, session_scope


async def create_user_profile(new_user_id: int) -> None:
    """Создание пользователя в БД (обычно по /start)."""
    async with session_scope(commit=True) as session:
        session.add(User(user_id=new_user_id))


async def check_user_exists(new_user_id: int) -> bool:
    """Проверка существования анкеты."""
    async with session_scope() as session:
        user_id = await session.scalar(
            select(User.user_id).where(User.user_id == new_user_id)
        )
        return user_id is not None


async def block_user(owner_user_id: int, blocked_user_id: int) -> None:
    """Блокировка пользователя blocked_user_id пользователем owner_user_id, если он ещё не заблокирован."""
    async with session_scope(commit=True) as session:
        exists = await session.scalar(
            select(1)
            .where(
                Blacklist.owner_id == owner_user_id,
                Blacklist.blocked_user_id == blocked_user_id,
            )
            .limit(1)
        )
        if exists is None:
            session.add(
                Blacklist(owner_id=owner_user_id, blocked_user_id=blocked_user_id)
            )


async def clean_blacklist(owner_user_id: int) -> bool:
    """Очистка черного списка пользователя owner_user_id"""
    async with session_scope(commit=True) as session:
        exists = await session.scalar(
            select(1).where(Blacklist.owner_id == owner_user_id).limit(1)
        )
        if exists is None:
            return False

        await session.execute(
            delete(Blacklist).where(Blacklist.owner_id == owner_user_id)
        )
        return True


async def check_if_user_blocked(
    blocked_user_id: int,
    owner_user_id: int,
) -> bool:
    """
    Проверка, заблокировал ли owner_user_id пользователя blocked_user_id
    Возвращает True, если заблокирован, иначе False
    """

    async with session_scope() as session:
        exists = await session.scalar(
            select(1)
            .where(
                Blacklist.owner_id == owner_user_id,
                Blacklist.blocked_user_id == blocked_user_id,
            )
            .limit(1)
        )
        return exists is not None
