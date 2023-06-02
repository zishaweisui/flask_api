from repositories import UsersRepository
from translators import UserTranslator, NoteTranslator
from infrastructure_exceptions import NotFoundException

class UsersService:
    def __init__(self, users_repositoty, user_translator):
        self.repository = users_repositoty
        self.translator = user_translator

    def get_all(self):
        user_records = self.repository.get_users()
        return [self.translator.from_database(record) for record in user_records]

    def get(self, user_id):
        user_record = self.repository.get_user(user_id)
        if not user_record:
            raise NotFoundException
        return self.translator.from_database(user_record)

    def create(self, user):
        return self.repository.create_user(user)

    def update(self, user_id, user):
        return self.repository.update_user(user_id, user)

    def delete(self, user_id):
        return self.repository.delete_user(user_id)

note_translator = NoteTranslator()
user_translator = UserTranslator(note_translator)
users_repository = UsersRepository()
users_service = UsersService(users_repository, user_translator)
