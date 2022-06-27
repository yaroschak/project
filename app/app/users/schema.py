import re
from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, validator
from pydantic.types import constr

_phone_template = re.compile(r'^\+380\d{9}$')


def is_valid_phone(phone: str) -> bool:
    result = _phone_template.match(phone)
    return bool(result)


def check_phone_number(phone_number: str) -> Optional[str]:
    if phone_number is not None and not is_valid_phone(phone_number):
        raise ValueError(f'The phone must by next format +380XXXXXXXXX')
    return phone_number


class UserBase(BaseModel):
    phone_number: Optional[str] = None
    nickname: Optional[str] = None


class UserCreate(UserBase):
    phone_number: str
    password: constr(min_length=6)

    # validators
    _phone_number = validator('phone_number', allow_reuse=True)(check_phone_number)


class UserUpdate(UserBase):
    password: Optional[constr(min_length=6)] = None

    # validators
    _phone_number = validator('phone_number', allow_reuse=True)(check_phone_number)


class UserInDBBase(UserBase):
    id: Optional[int] = None
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    hashed_password: str


class Users(BaseModel):
    result: List[User]
    skip: int = 0
    limit: int = 10
    total: int
