from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from .model import UserModel
from database import db_helper


async def get_user(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    """Get user with id"""
    user = await session.get(UserModel, user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="ReadUser not found"
    )
