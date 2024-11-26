from typing import List, Optional
from models import User, Task

users_db: List[User] = []

def create_user(user: User) -> User:
    users_db.append(user)
    return user

def get_user(user_id: int) -> Optional[User]:
    return next((u for u in users_db if u.id == user_id), None)

def update_user(user_id: int, updated_user: User) -> Optional[User]:
    global users_db
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db[index] = updated_user
            return updated_user
    return None

def delete_user(user_id: int) -> bool:
    global users_db
    initial_length = len(users_db)
    users_db = [u for u in users_db if u.id != user_id]
    return len(users_db) < initial_length
