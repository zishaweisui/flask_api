from models import User, users_schema

class GetUsersRepository:
    def get_all_users(self):
        users = User.query.all()
        return users_schema.dump(users)
        