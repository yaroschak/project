from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base, TimestampMixin


class Task(TimestampMixin, Base):
    __tablename__ = 'task'  # noqa:

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    is_done = Column(Boolean)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")
