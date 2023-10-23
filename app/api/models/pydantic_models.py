from typing import Union
from pydantic import BaseModel, EmailStr, field_validator
from fastapi import HTTPException


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

    @field_validator('username')
    def username_validate(cls, val: str):
        result = val.isalpha()
        if result and len(val) >= 3:
            return val
        else:
            raise HTTPException(
                status_code=400,
                detail='The username must contain only letters and consist of 3 or more characters'
            )

    @field_validator('full_name')
    def full_name_is_alpha(cls, val: str):
        if val is None:
            return None
        elif val.replace(' ', '').isalpha():
            return val
        else:
            raise HTTPException(
                status_code=400,
                detail='The full name must contain only letters'
            )


# расширяем класс User, добавляя новый атрибут
class UserInDB(User):
    hashed_password: str


class CurrencyExch(BaseModel):
    value_1: str
    value_2: str
    quantity: float = 1

    @field_validator('value_1')
    def value_1_validate(cls, val: str):
        if len(val) == 3:
            return val
        else:
            raise HTTPException(
                status_code=400,
                detail='The value must be 3 characters'
            )

    @field_validator('value_2')
    def value_2_validate(cls, val: str):
        if len(val) == 3:
            return val
        else:
            raise HTTPException(
                status_code=400,
                detail='The value must be 3 characters'
            )
