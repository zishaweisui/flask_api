from flask import request
from handlers.base_handler import BaseHandler
from services.update_user_service import UpdateUserService

class UpdateUserHandler(BaseHandler):
    def __init__(self):
        self.service = UpdateUserService()

    def update_user(self, **kwargs):
        return self.service.update(kwargs['user_id'], request.get_json())
        