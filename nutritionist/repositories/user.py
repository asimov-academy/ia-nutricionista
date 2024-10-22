from typing import Optional, List
from tinydb import Query
from nutritionist.models import User
from nutritionist.repositories.base_repository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.user_table = self.get_table('users')

    def create_user(
        self,
        telegram_id: int,
        name: str,
        sex: str,
        age: str,
        height_cm: str,
        weight_kg: str,
        has_diabetes: str,
        goal: str
    ) -> User:
        user = User(
            telegram_id=telegram_id,
            name=name,
            sex=sex,
            age=age,
            height_cm=height_cm,
            weight_kg=weight_kg,
            has_diabetes=has_diabetes,
            goal=goal
        )
        self.user_table.insert(user.model_dump())
        return user

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        UserQuery = Query()
        result = self.user_table.get(UserQuery.id == user_id)
        return User(**result) if result else None

    def get_user_by_telegram_id(self, telegram_id: str) -> Optional[User]:
        UserQuery = Query()
        result = self.user_table.get(UserQuery.telegram_id == telegram_id)
        return User(**result) if result else None

    def update_user(
        self,
        telegram_id: int,
        name: str,
        sex: str,
        age: str,
        height_cm: str,
        weight_kg: str,
        has_diabetes: str,
        goal: str
    ) -> Optional[User]:
        update_data = {
            "name": name,
            "sex": sex,
            "age": age,
            "height_cm": height_cm,
            "weight_kg": weight_kg,
            "has_diabetes": has_diabetes,
            "goal": goal
        }

        UserQuery = Query()
        self.user_table.update(update_data, UserQuery.telegram_id == telegram_id)
        updated_user = self.get_user_by_telegram_id(telegram_id)
        return updated_user

    def delete_user(self, user_id: int) -> None:
        UserQuery = Query()
        self.user_table.remove(UserQuery.id == user_id)

    def get_all_users(self) -> List[User]:
        all_users = self.user_table.all()
        return [User(**user) for user in all_users]
