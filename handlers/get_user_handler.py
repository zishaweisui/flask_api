from handlers.base_handler import BaseHandler

class GetUserHandler(BaseHandler):
    def __init__(self, users_service):
        self.service = users_service
    
    def get_user(self, **kwargs):
        return self.service.get(kwargs['user_id'])
