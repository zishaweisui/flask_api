from handlers.base_handler import BaseHandler
from services.user_service import UserService

class GetUsersHandler(BaseHandler):
    def __init__(self):
        self.service = UserService()
    
    def get_users(self):
        return self.service.read_all()
