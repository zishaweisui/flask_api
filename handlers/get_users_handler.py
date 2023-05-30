from handlers.base_handler import BaseHandler

class GetUsersHandler(BaseHandler):
    def __init__(self, users_service, presenter=None):
        super().__init__(presenter)
        self.service = users_service
    
    def get_users(self):
        return self.service.get_all()
