from repositories.create_user_repo import CreateUserRepository

class CreateUserService:
    def __init__(self):
        self.repo = CreateUserRepository()

    def create(self, user):
        return self.repo.create_user(user)
