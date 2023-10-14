from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from core.security import (
    get_current_active_user,
    OAuth2PasswordRequestForm,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    authenticate_user,
    get_password_hash
)
from api.models.pydantic_models import User, Token, UserInDB
from datetime import timedelta
from db import create_new_user

router = APIRouter()


# при успешной аутентификации генерируется токен доступа
@router.post('/login', response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
            )
    # время истечения токена и его создание
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.username}, expires_delta=access_token_expires
    )
    # ответ должен содержать поля token_type, access_token (токен доступа)
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/me')
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{'item_id': 'succesfull', 'owner': current_user.username}]


@router.post('/register')
async def registration_user(user: Annotated[User, Depends()], password: str):
    password_hash = get_password_hash(password)
    # делаем словарь для добавления хэша пароля
    user = user.model_dump()
    user.update({'hashed_password': password_hash})
    # создаем объект класса c паролем
    user = UserInDB(**user)
    # можно добавить обработку повторений (вывод ошибки при повторении),
    # сейчас идет игнорирование добавления в БД при наличии записи
    create_new_user(user)
    return {'message': 'seccesfull'}
