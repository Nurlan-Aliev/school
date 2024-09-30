from sqlalchemy import select
from sqlalchemy import ext
from sqlalchemy.ext.asyncio import AsyncSession
from .schema import CreateUser, UpdateUser
from .model import UserModel
from src.user.utils import hash_password


async def create_user(user_in: CreateUser, session: AsyncSession) -> UserModel:
    """Add new user in Database"""
    user = user_in.model_dump()
    user["password"] = hash_password(user["password"])
    user_model = UserModel(**user)
    session.add(user_model)
    await session.commit()
    return user_model


async def update_user(
    user: UserModel,
    user_in: UpdateUser,
    session: AsyncSession,
) -> UserModel:

    user.name = user_in.name if user_in.name else user.name
    user.surname = user_in.surname if user_in.surname else user.surname
    user.age = user_in.age if user_in.age else user.age
    user.username = user_in.username if user_in.username else user.username
    user.email_address = (
        user_in.email_address if user_in.email_address else user.email_address
    )

    await session.commit()
    return user


async def delete_user(
    user: UserModel,
    session: AsyncSession,
):

    await session.delete(user)
    await session.commit()
    return f"user {user.name} was deleted"
