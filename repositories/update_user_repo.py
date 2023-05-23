from config import db
from models import User, user_schema

class UpdateUserRepository:
    def update_user(self, user_id, user):
        existing_user = User.query.filter(User.id == user_id).one_or_none()

        if existing_user:
            update_user = user_schema.load(user, session=db.session)
            existing_user.fname = update_user.fname
            existing_user.lname = update_user.lname
            db.session.merge(existing_user)
            db.session.commit()
            return user_schema.dump(existing_user), 200
