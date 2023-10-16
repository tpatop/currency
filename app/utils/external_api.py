from requests import get, Response
from core.config import load_api_currency
from api.models.pydantic_models import CurrencyExch


config = load_api_currency()
API_KEY_CURRENCY = config.key

URL = "https://api.apilayer.com/currency_data/"
headers = {'apikey': API_KEY_CURRENCY}


def requests_currency_list():
    response: Response = get(
        url=URL + 'list',
        headers=headers,
        data={}
    )
    response = response.json()['currencies']
    return response


def checking_values_in_list(exchange: CurrencyExch):
    curr_list = requests_currency_list()
    # исключаем ошибку с регистром
    exchange.value_1 = exchange.value_1.upper()
    exchange.value_2 = exchange.value_2.upper()
    # исключаем ошибку с отсутсвием в поддержке внешнего API кода валюты
    # минус способа: два запроса к внешнему API
    result = all([exchange.value_1 in curr_list,
                  exchange.value_2 in curr_list])
    return result


def currency_convert(exchange: CurrencyExch):
    url = URL + f'convert?to={exchange.value_1}&from={exchange.value_2}&amount={exchange.quantity}'
    response: Response = get(
        url=url,
        headers=headers,
        data={}
    )
    return response.json()
