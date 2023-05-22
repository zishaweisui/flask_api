from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def read_all(self):
        return self.repo.get_all_users()

    def read_one(self, user_id):
        return self.repo.get_one_user(user_id)

    def create(self, user):
        return self.repo.create_user(user)

    def update(self, user_id, user):
        return self.repo.update_user(user_id, user)

    def delete(self, user_id):
        return self.repo.delete_user(user_id)
