from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from core.security import (
    fake_hash_password,
    oauth2_scheme,
    OAuth2PasswordRequestForm
)
from api.models.user import User, UserInDB
from db import get_user

Router = APIRouter()


# @Router.get('/register')
# async def registration_user(token: Annotated[str, Depends(oauth2_sheme)]):
#     # Конечная точка для регистрации пользователей
#     return {'token': token}


# @Router.get('/login')
# async def login_user():
#     # Конечная точка входа для генерации токенов для аутентификации
#     pass


def fake_decode_token(token):
    # просто пример (нулевой ур. безопасности)
    user = get_user(token)
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail='Inactive user')
    return current_user


@Router.post('/token')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # проверка наличия пользователя в БД
    user = get_user(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    # проверка совпадения хэшей паролей введенных пользователем и сохр. в БД
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail='Incorrect username or password')

    # ответ должен содержать поля token_type, access_token (токен доступа)
    # сейчас небезопасно, ибо возвращается просто имя
    return {'access_token': user.username, 'token_type': 'bearer'}


@Router.get('/me')
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user
