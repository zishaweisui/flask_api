from handlers.base_handler import BaseHandler
from services.get_user_service import GetUserService

class GetUserHandler(BaseHandler):
    def __init__(self):
        self.service = GetUserService()
    
    def get_user(self, **kwargs):
        return self.service.read_one(kwargs['user_id'])
