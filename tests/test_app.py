import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.api.models.pydantic_models import User


@pytest.fixture(scope='module')
def client():
    client = TestClient(app)
    yield client


def test_user_endpoints_non_auth(client):
    # не авторизованный пользователь
    responce = client.get('/auth/me')
    assert responce.status_code == 401


def test_user_registration(client):

    # data = {'user': User(username='sixe').model_dump(),
    #         'password': '12345'}
    password = '12345'
    username = 'user'
    # print(data)
    s = f'/auth/register?password={password}&username={username}'
    print(s)
    responce = client.post(s)
    # responce = client.post('/auth/register', json=data)
    assert responce.status_code == 200
    assert responce.json() == {
        'message': 'seccesfull'
    }
