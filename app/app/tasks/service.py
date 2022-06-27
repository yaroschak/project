from typing import Tuple, List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..users.service import UserService
from . import model, schema, crud


class TaskService:

    @staticmethod
    def get_list(db: Session, *,
                 skip: int,
                 limit: int
                 ) -> Tuple[List[model.Task], int]:
        tasks = crud.task.get_multi(db, skip=skip, limit=limit)
        total = crud.task.count(db)
        return tasks, total

    @staticmethod
    def create(db: Session, *, task_in: schema.TaskCreate) -> model.Task:

        UserService.read(db, user_id=task_in.user_id)
        task = crud.task.create(db=db, obj_in=task_in)
        return task

    @staticmethod
    def read(db: Session, *, task_id: int) -> schema.Task:

        task = crud.task.get(db=db, id=task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    @staticmethod
    def update(db: Session, *, task: model.Task,
               task_in: schema.TaskUpdate) -> model.Task:

        if task_in.user_id:
            UserService.read(db, user_id=task_in.user_id)
        task = crud.task.update(db=db, db_obj=task, obj_in=task_in)
        return task

    @staticmethod
    def delete(db: Session, *, task: model.Task) -> model.Task:
        task = crud.task.remove(db=db, id=task.id)
        return task
