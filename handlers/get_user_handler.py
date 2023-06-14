from handlers.base_handler import BaseHandler

class GetUserHandler(BaseHandler):
    def __init__(self, users_service, presenter):
        super().__init__(presenter)
        self.service = users_service
    
    def get_user(self, **kwargs):
        return self.execute(
            self.service.get,
            kwargs['user_id']
        )
