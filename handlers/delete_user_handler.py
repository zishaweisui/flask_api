from handlers.base_handler import BaseHandler
from services.user_service import UserService

class DeleteUserHandler(BaseHandler):
    def __init__(self):
        self.service = UserService()

    def delete_user(self, **kwargs):
        return self.service.delete(kwargs['user_id'])
        