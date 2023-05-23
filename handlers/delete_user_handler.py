from handlers.base_handler import BaseHandler
from services.delete_user_service import DeleteUserService

class DeleteUserHandler(BaseHandler):
    def __init__(self):
        self.service = DeleteUserService()

    def delete_user(self, **kwargs):
        return self.service.delete(kwargs['user_id'])
        