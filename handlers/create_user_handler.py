from flask import request
from handlers.base_handler import BaseHandler
from services.create_user_service import CreateUserService

class CreateUserHandler(BaseHandler):
    def __init__(self):
        self.service = CreateUserService()

    def create_user(self):
        return self.service.create(request.get_json())
