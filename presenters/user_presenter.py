class UserPresenter:
    def __init__(self, user):
        self.user = user
        
    def present(self):
        return {
            "fname": self.user.get('fname'),
            "id": self.user.get('id'),
            "lname": self.user.get('lname'),
            "notes": self.user.get('notes', []),
            "timestamp": self.user.get('timestamp')
        }
