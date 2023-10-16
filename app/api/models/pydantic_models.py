from typing import Union
from pydantic import BaseModel, EmailStr, validator


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    email: Union[EmailStr, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

    @validator('username')
    def username_validate(cls, val: str):
        result = val.isalpha()
        if result and len(val) > 3:
            return val
        else:
            raise ValueError('The username must contain only letters and consist of 4 or more characters')

    @validator('full_name')
    def full_name_is_alpha(cls, val: str):
        if val is not None and val.replace(' ', '').isalpha():
            return val
        else:
            raise ValueError('The full name must contain only letters')


# расширяем класс User, добавляя новый атрибут
class UserInDB(User):
    hashed_password: str


class CurrencyExch(BaseModel):
    value_1: str
    value_2: str
    quantity: float = 1

    @validator('value_1')
    def value_1_validate(cls, val: str):
        if len(val) == 3:
            return val
        else:
            raise ValueError('The value must be 3 characters')

    @validator('value_2')
    def value_2_validate(cls, val: str):
        if len(val) == 3:
            return val
        else:
            raise ValueError('The value must be 3 characters')
