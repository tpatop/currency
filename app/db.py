from api.models.user import UserInDB


#  БД для тестирования правильности работы
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


def get_user(username: str, db=fake_users_db):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)