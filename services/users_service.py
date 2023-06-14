from repositories import UsersRepository
from translators import UserTranslator, NoteTranslator
from models import PlainUser
from infrastructure_exceptions import NotFoundException

class UsersService:
    def __init__(self, users_repository):
        self.repository = users_repository

    def get_all(self):
        return self.repository.get_users()

    def get(self, user_id):
        user = self.repository.get_user(user_id)
        if not user:
            raise NotFoundException
        return user

    def create(self, attributes):
        user = PlainUser(**attributes)
        # user["created_date"] = datetime.utcnow()-timedelta(days=30)
        return self.repository.create_user(user)

    def update(self, user_id, attributes):
        user = PlainUser(**attributes)
        return self.repository.update_user(user_id, user)

    def delete(self, user_id):
        return self.repository.delete_user(user_id)

note_translator = NoteTranslator()
user_translator = UserTranslator(note_translator)
users_repository = UsersRepository(user_translator)
users_service = UsersService(users_repository)
