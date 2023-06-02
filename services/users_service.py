from repositories import UsersRepository
from infrastructure_exceptions import NotFoundException

class UsersService:
    def __init__(self, users_repositoty):
        self.repository = users_repositoty

    def get_all(self):
        return self.repository.get_users()

    def get(self, user_id):
        user = self.repository.get_user(user_id)
        if not user:
            raise NotFoundException
        return user

    def create(self, user):
        return self.repository.create_user(user)

    def update(self, user_id, user):
        return self.repository.update_user(user_id, user)

    def delete(self, user_id):
        return self.repository.delete_user(user_id)


users_repository = UsersRepository()
users_service = UsersService(users_repository)
