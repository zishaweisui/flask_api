from handlers.base_handler import BaseHandler
from services.user_service import UserService

class GetUserHandler(BaseHandler):
    def __init__(self):
        self.service = UserService()
    
    def get_user(self, **kwargs):
        return self.service.read_one(kwargs['user_id'])
