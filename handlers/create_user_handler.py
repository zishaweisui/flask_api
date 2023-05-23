from flask import request
from handlers.base_handler import BaseHandler
from services.user_service import UserService

class CreateUserHandler(BaseHandler):
    def __init__(self):
        self.service = UserService()

    def create_user(self):
        return self.service.create(request.get_json())
