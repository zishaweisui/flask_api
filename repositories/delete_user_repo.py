from flask import make_response
from config import db
from models import User

class DeleteUserRepository:
    def delete_user(self, user_id):
        existing_user = User.query.filter(User.id == user_id).one_or_none()

        if existing_user:
            db.session.delete(existing_user)
            db.session.commit()
            return make_response(f"User successfully deleted", 200)
            