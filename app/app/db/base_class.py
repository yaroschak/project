import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, func


class TimestampMixin(object):

    created_at = Column(DateTime, server_default=func.current_timestamp())
    updated_at = Column(DateTime, server_default=func.current_timestamp(), onupdate=datetime.datetime.utcnow)


Base = declarative_base()
