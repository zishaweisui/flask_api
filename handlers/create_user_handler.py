from flask import request
from handlers.base_handler import BaseHandler

class CreateUserHandler(BaseHandler):
    def __init__(self, users_service):
        self.service = users_service

    def create_user(self):
        return self.service.create(request.get_json())
