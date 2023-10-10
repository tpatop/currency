from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from core.security import (
    get_current_active_user,
    OAuth2PasswordRequestForm,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    authenticate_user
)
from api.models.user import User, Token
from datetime import timedelta

Router = APIRouter()


@Router.post('/token', response_model=Token)
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


@Router.get('/me')
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{'item_id': 'Succesfull', 'owner': current_user.username}]
