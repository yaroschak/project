# Import all the models, so that Base has them before being
# imported by Alembic
# Важливо для створення автоміграції

from .base_class import Base, TimestampMixin
from app.users.model import User
from app.tasks.model import Task
