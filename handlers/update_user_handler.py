from flask import request
from handlers.base_handler import BaseHandler
from services.user_service import UserService

class UpdateUserHandler(BaseHandler):
    def __init__(self):
        self.service = UserService()

    def update_user(self, **kwargs):
        return self.service.update(kwargs['user_id'], request.get_json())
        