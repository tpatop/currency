from typing import Union
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


# расширяем класс User, добавляя новый атрибут
class UserInDB(User):
    hashed_password: str


class CurrencyExch(BaseModel):
    value_1: str
    value_2: str
    quantity: float = 1
