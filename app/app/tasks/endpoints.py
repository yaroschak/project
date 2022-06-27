from typing import Any

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api import dependencies as deps

from ..users.model import User
from . import schema
from .service import TaskService

router = APIRouter()


@router.get("/",
            response_model=schema.Tasks,
            response_model_exclude_none=True,
            )
def read_tasks(
        db: Session = Depends(deps.get_db),
        skip: int = Query(default=0, ge=0),
        limit: int = Query(default=10, gt=0, le=500),
        current_user: User = Depends(deps.get_current_user),  # noqa:
) -> Any:
    tasks, total = TaskService.get_list(db, skip=skip, limit=limit)

    return schema.Tasks(result=tasks, skip=skip, limit=limit, total=total)


@router.post("/",
             response_model=schema.TaskInDBBase,
             response_model_exclude_none=True,
             )
def create_task(
        *,
        db: Session = Depends(deps.get_db),
        task_in: schema.TaskCreate,
        current_user: User = Depends(deps.get_current_user),
) -> Any:
    return TaskService.create(db, task_in=task_in)


@router.get("/{id}",
            response_model=schema.Task,
            response_model_exclude_none=True,

            )
def read_task(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: User = Depends(deps.get_current_user)
) -> Any:
    return TaskService.read(db, task_id=id)


@router.put("/{id}",
            response_model=schema.TaskInDBBase,
            response_model_exclude_none=True,

            )
def update_task(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        task_in: schema.TaskUpdate,
        current_user: User = Depends(deps.get_current_user),  # noqa:
) -> Any:
    task = TaskService.read(db, task_id=id)
    task = TaskService.update(db, task=task, task_in=task_in)
    return task


@router.delete("/{id}",
               response_model=schema.TaskInDBBase,
               response_model_exclude_none=True,

               )
def delete_dtask(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: User = Depends(deps.get_current_user),  # noqa:
) -> Any:
    task = TaskService.read(db, task_id=id)

    task = TaskService.delete(db, task=task)

    return task
