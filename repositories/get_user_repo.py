from models import User, user_schema

class GetUserRepository:
    def get_one_user(self, user_id):
        user = User.query.filter(User.id == user_id).one_or_none()
        if user is not None:
            return user_schema.dump(user)
            