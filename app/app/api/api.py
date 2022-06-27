from fastapi import APIRouter

from app.login import endpoints as login
from app.users import endpoints as users
from app.tasks import endpoints as tasks

api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(tasks.router, prefix="/users/me/tasks", tags=["users.tasks"])
