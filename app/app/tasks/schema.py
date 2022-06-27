from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel


class TaskBase(BaseModel):
    description: Optional[str]
    is_done: bool = False
    user_id: Optional[int] = None


class TaskCreate(TaskBase):
    description: str
    user_id: int


class TaskUpdate(TaskBase):
    pass


class TaskInDBBase(TaskBase):
    id: Optional[int] = None

    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True


class Task(TaskInDBBase):
    pass


class Tasks(BaseModel):
    result: List[Task]
    skip: int = 0
    limit: int = 10
    total: int
