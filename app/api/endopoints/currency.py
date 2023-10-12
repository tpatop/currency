from fastapi import APIRouter, Depends
from typing import Annotated
from api.models.user import CurrencyExch, User
from core.security import get_current_active_user
from core.config import load_api_currency


config = load_api_currency()
API_KEY_CURRENCY = config.key


Router = APIRouter()


@Router.get('/exchange/')
async def exchange_currency(
    exchange: Annotated[CurrencyExch, Depends()],
    currect_user: Annotated[User, Depends(get_current_active_user)]
):
    return {'message': {currect_user.username: exchange.value_1}}


@Router.get('/list')
async def get_currency_list(
    currect_user: Annotated[User, Depends(get_current_active_user)]
):
    pass
