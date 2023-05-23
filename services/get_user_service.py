from repositories.get_user_repo import GetUserRepository

class GetUserService:
    def __init__(self):
        self.repo = GetUserRepository()

    def read_one(self, user_id):
        return self.repo.get_one_user(user_id)
