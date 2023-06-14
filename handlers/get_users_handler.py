from handlers.base_handler import BaseHandler

class GetUsersHandler(BaseHandler):
    def __init__(self, users_service, presenter):
        super().__init__(presenter)
        self.service = users_service
    
    def get_users(self):
        users = self.service.get_all()
        return [self.presenter.present(user) for user in users]
