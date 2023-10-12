from environs import Env
from pydantic import BaseModel


class HashConfig(BaseModel):
    secret_key: str
    algoritm: str
    expire_minutes: int


def load_hash_config(path: str | None = None):
    env = Env()
    env.read_env(path)

    return HashConfig(
        secret_key=env('SECRET_KEY'),
        algoritm=env('ALGORITHM'),
        expire_minutes=env('ACCESS_TOKEN_EXPIRE_MINUTES')
    )


class APICurrncy(BaseModel):
    key: str


def load_api_currency(path: str | None = None):
    env = Env()
    env.read_env(path)

    return APICurrncy(
        key=env('API_CURRENCY')
    )
