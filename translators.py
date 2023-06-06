from models import PlainUser, PlainNote

class UserTranslator:
    def __init__(self, note_translator):
        self.note_translator = note_translator

    def to_database(self, user: PlainUser):
        return {
            "id": user.id,
            "fname": user.fname,
            "lname": user.lname,
            "created_date": user.created_date,
            "updated_date": user.updated_date,
            "notes": [self.note_translator.to_database(note) for note in user.notes],
        }


    def from_database(self, user: PlainUser):
        return {
            "id": user.id,
            "fname": user.fname,
            "lname": user.lname,
            "created_date": user.created_date,
            "updated_date": user.updated_date,
            "notes": [self.note_translator.from_database(note) for note in user.notes],
        }
        

class NoteTranslator:
    def to_database(self, note):
        return {
            "id": note.get("id"),
            "user_id": note.get("user_id"),
            "content": note.get("content"),
            "created_date": note.get("created_date"),
            "updated_date": note.get("updated_date"),
        }

    def from_database(self, note: PlainNote):
        return {
            "id": note.id,
            "user_id": note.user_id,
            "content": note.content,
            "created_date": note.created_date,
            "updated_date": note.updated_date,
        }
