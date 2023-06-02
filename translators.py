from models import user_schema, note_schema, User

class UserTranslator:
    def __init__(self, note_translator):
        self.note_translator = note_translator

    def from_database(self, record):
        try:
            user_dict = user_schema.dump(record)
            user = User(**user_dict)
            return user
        except Exception as e:
            print(record)
            print("Error: ", e)
            raise

class NoteTranslator:
    def from_database(self, record):
        note_dict = note_schema.dump(record)
        note = note_schema.load(note_dict)
        return note
