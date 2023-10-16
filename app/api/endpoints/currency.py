from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from api.models.pydantic_models import CurrencyExch
from core.security import get_current_active_user
from utils.external_api import (
    requests_currency_list,
    currency_convert,
    checking_values_in_list
)


router = APIRouter()


@router.get('/list', dependencies=[Depends(get_current_active_user)])
async def get_currency_list():
    data = requests_currency_list()
    return data


@router.get('/exchange/', dependencies=[Depends(get_current_active_user)])
async def exchange_currency(exchange: Annotated[CurrencyExch, Depends()]):
    if checking_values_in_list(exchange):
        data = currency_convert(exchange)
        return data
    else:
        raise HTTPException(
            status_code=400,
            detail={'message': 'Incorrect currency code',
                    'recommendation': 'You can view a list of all supported currency codes by downloading it at ".../currency/list"'}
        )
