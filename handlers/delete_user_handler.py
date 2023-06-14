from handlers.base_handler import BaseHandler

class DeleteUserHandler(BaseHandler):
    def __init__(self, users_service):
        self.service = users_service

    def delete_user(self, **kwargs):
        return self.service.delete(kwargs['user_id'])
        