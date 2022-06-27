from typing import Tuple, List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import model, schema, crud


class UserService:

    @staticmethod
    def get_list(db: Session, *,
                 skip: int,
                 limit: int,
                 ) -> Tuple[List[model.User], int]:
        users = crud.user.get_multi(db,  skip=skip, limit=limit)
        total = crud.user.count(db)
        return users, total

    @staticmethod
    def create(db: Session, *, user_in: schema.UserCreate) -> model.User:
        user = crud.user.get_by_phone_number(db, phone_number=user_in.phone_number)
        if user:
            raise HTTPException(
                status_code=400,
                detail="The user with this username already exists in the system.",
            )

        user = crud.user.create(db, obj_in=user_in)
        return user

    @staticmethod
    def read(db: Session, *, user_id: int) -> model.User:
        user = crud.user.get(db, id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def update(db: Session, *, user: model.User, user_in: schema.UserUpdate) -> model.User:
        user = crud.user.update(db, db_obj=user, obj_in=user_in)
        return user

    @staticmethod
    def delete(db: Session, *, user: model.User) -> model.User:
        user = crud.user.remove(db=db, id=user.id)
        return user
