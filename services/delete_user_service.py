from repositories.delete_user_repo import DeleteUserRepository

class DeleteUserService:
    def __init__(self):
        self.repo = DeleteUserRepository()
    
    def delete(self, user_id):
        return self.repo.delete_user(user_id)
    