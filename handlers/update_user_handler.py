from flask import request
from handlers.base_handler import BaseHandler

class UpdateUserHandler(BaseHandler):
    def __init__(self, users_service):
        self.service = users_service

    def update_user(self, **kwargs):
        return self.service.update(kwargs['user_id'], request.get_json())
        