from flask import make_response
from config import db
from models import User, users_schema, user_schema

class UserRepository:
    def get_all_users(self):
        users = User.query.all()
        return users_schema.dump(users)

    def get_one_user(self, user_id):
        user = User.query.filter(User.id == user_id).one_or_none()
        if user is not None:
            return user_schema.dump(user)

    def create_user(self, user):
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 200

    def update_user(self, user_id, user):
        existing_user = User.query.filter(User.id == user_id).one_or_none()

        if existing_user:
            update_user = user_schema.load(user, session=db.session)
            existing_user.fname = update_user.fname
            existing_user.lname = update_user.lname
            db.session.merge(existing_user)
            db.session.commit()
            return user_schema.dump(existing_user), 200

    def delete_user(self, user_id):
        existing_user = User.query.filter(User.id == user_id).one_or_none()

        if existing_user:
            db.session.delete(existing_user)
            db.session.commit()
            return make_response(f"User successfully deleted", 200)
