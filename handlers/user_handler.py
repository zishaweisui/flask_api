from flask import request
from handlers.base_handler import BaseHandler
from services.user_service import UserService
from .exceptions import UserNotFoundError

class UserHandler(BaseHandler):
    def __init__(self):
        self.service = UserService()

    def routes(self, *args, **kwargs):
        if request.method == 'GET':
            if 'user_id' in kwargs:
                return self.service.read_one(kwargs['user_id'])
            else:
                return self.service.read_all()
        elif request.method == 'POST':
            return self.service.create(request.get_json())
        elif request.method == 'PUT':
            return self.service.update(kwargs['user_id'], request.get_json())
        elif request.method == 'DELETE':
            return self.service.delete(kwargs['user_id'])
        else:
            raise UserNotFoundError
