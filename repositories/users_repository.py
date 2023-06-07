from config import db
from models import User

class UsersRepository:
    def __init__(self, user_translator):
        self.translator = user_translator

    def get_users(self):
        users = User.query.all()
        return users

    def get_user(self, user_id):
        user = User.query.filter(User.id == user_id).one_or_none()
        return user

    def create_user(self, plain_user):
        user = self.translator.to_database(plain_user)
        new_user = User(**user)
        db.session.add(new_user)
        db.session.commit()
        return self.translator.from_database(new_user)

    def update_user(self, user_id, plain_user):
        user = self.translator.to_database(plain_user)
        new_user = {'lname': user.get('lname'), 'fname': user.get('fname')}
        User.query.filter(User.id == user_id).update(new_user)
        updated_user = User.query.filter(User.id == user_id).one_or_none()
        db.session.commit()
        return self.translator.from_database(updated_user)

    def delete_user(self, user_id):
        existing_user = User.query.filter(User.id == user_id).one_or_none()

        if existing_user:
            db.session.delete(existing_user)
            db.session.commit()
            return existing_user
