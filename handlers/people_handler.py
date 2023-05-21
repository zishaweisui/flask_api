from flask import request
from .base_handler import BaseHandler
from services.people_service import PeopleService
from ..exceptions import UserNotFoundError

class PeopleHandler(BaseHandler):
    def __init__(self):
        self.service = PeopleService()

    def routes(self, *args, **kwargs):
        if request.method == 'GET':
            if 'person_id' in kwargs:
                return self.service.read_one(kwargs['person_id'])
            else:
                return self.service.read_all()
        elif request.method == 'POST':
            return self.service.create(request.get_json())
        elif request.method == 'PUT':
            return self.service.update(kwargs['person_id'], request.get_json())
        elif request.method == 'DELETE':
            return self.service.delete(kwargs['person_id'])
        else:
            raise UserNotFoundError
