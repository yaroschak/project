from typing import Any, List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api import dependencies as deps

from . import schema, model
from .service import UserService

router = APIRouter()


@router.get("/",
            response_model=schema.Users,
            response_model_exclude_none=True,
            )
def read_users(
        db: Session = Depends(deps.get_db),
        skip: int = Query(default=0, ge=0),
        limit: int = Query(default=10, gt=0, le=500),
        current_user: model.User = Depends(deps.get_current_user),
) -> Any:
    users, total = UserService.get_list(db, skip=skip, limit=limit)
    return schema.Users(result=users, skip=skip, limit=limit, total=total)


@router.post("/",
             response_model=schema.UserInDBBase,
             response_model_exclude_none=True,
             )
def create_user(
        *,
        db: Session = Depends(deps.get_db),
        user_in: schema.UserCreate,
) -> Any:
    user = UserService.create(db, user_in=user_in)
    return user


@router.get("/me",
            response_model=schema.User,
            response_model_exclude_none=True,
            )
def read_user(
        current_user: model.User = Depends(deps.get_current_user),
) -> Any:
    return current_user


@router.put("/me",
            response_model=schema.UserInDBBase,
            response_model_exclude_none=True,
            )
def update_user(
        *,
        db: Session = Depends(deps.get_db),
        user_in: schema.UserUpdate,
        current_user: model.User = Depends(deps.get_current_user),
) -> Any:
    return UserService.update(db, user=current_user, user_in=user_in)


@router.delete("/me",
               response_model=schema.UserInDBBase,
               response_model_exclude_none=True,
               )
def delete_user(
        *,
        db: Session = Depends(deps.get_db),
        current_user: model.User = Depends(deps.get_current_user),  # noqa:
) -> Any:
    return UserService.delete(db, user=current_user)
