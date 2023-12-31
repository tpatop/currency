from api.models.pydantic_models import UserInDB


#  БД для тестирования правильности работы
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


def get_user(username: str, db=fake_users_db):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def create_new_user(user: UserInDB):
    if user.username not in fake_users_db:
        fake_users_db[user.username] = user.model_dump()
    print(*fake_users_db.items(), sep='\n')
