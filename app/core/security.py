from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# 'token' ~ './token' - путь до конечной точки, в которой реализована аутентфикация
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')


def fake_hash_password(password: str) -> str:
    return 'fakehashed' + password
