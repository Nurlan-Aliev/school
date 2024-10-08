from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status
from .schema import ReadUser, CreateUser, UpdateUser
from . import crud
from database import db_helper
from src.user import depends
from src.user.model import UserModel


router = APIRouter(tags=["user"], prefix="/user")


@router.get("/{user_id}", response_model=ReadUser)
async def get_user(
    user: UserModel = Depends(depends.get_user),
):
    """Get user with id"""

    return user


@router.post("/", response_model=ReadUser)
async def create_user(
    user_in: CreateUser,
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    """Create new user"""
    return await crud.create_user(user_in=user_in, session=session)


@router.patch("/{user_id}", response_model=ReadUser)
async def update_user(
    user_in: UpdateUser,
    user: UserModel = Depends(depends.get_user),
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.update_user(user, user_in, session)


@router.delete("/{user_id}")
async def delete_user(
    user: UserModel = Depends(depends.get_user),
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.delete_user(user, session)
