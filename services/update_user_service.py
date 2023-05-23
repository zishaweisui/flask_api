from repositories.update_user_repo import UpdateUserRepository

class UpdateUserService:
    def __init__(self):
        self.repo = UpdateUserRepository()

    def update(self, user_id, user):
        return self.repo.update_user(user_id, user)
