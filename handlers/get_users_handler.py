from handlers.base_handler import BaseHandler
from services.get_users_service import GetUsersService

class GetUsersHandler(BaseHandler):
    def __init__(self):
        self.service = GetUsersService()
    
    def get_users(self):
        return self.service.read_all()
