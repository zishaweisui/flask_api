from config import db
from models import user_schema

class CreateUserRepository:
    def create_user(self, user):
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 200
