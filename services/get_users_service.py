from repositories.get_users_repo import GetUsersRepository
class GetUsersService:
    def __init__(self):
        self.repo = GetUsersRepository()

    def read_all(self):
        return self.repo.get_all_users()
