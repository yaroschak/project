from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..db.base_class import Base, TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = 'user'  # noqa:

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    nickname = Column(String)
    hashed_password = Column(String, nullable=False)
