from requests import get, Response
from core.config import load_api_currency
from api.models.user import CurrencyExch


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


def currency_convert(exchange: CurrencyExch):
    url = URL + f'convert?to={exchange.value_1}&from={exchange.value_2}&amount={exchange.quantity}'
    response: Response = get(
        url=url,
        headers=headers,
        data={}
    )
    return response.json()
