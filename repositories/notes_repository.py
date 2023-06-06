from config import db
from models import Note

class NotesRepository:
    def __init__(self, note_translator):
        self.translator = note_translator

    def get_note(self, note_id):
        note = Note.query.get(note_id)
        if note is not None:
            return self.translator.from_database(note)
        return None

    def create_note(self, note):
        note_dict = self.translator.to_database(note)
        new_note = Note(**note_dict)
        db.session.add(new_note)
        db.session.commit()
        return self.translator.from_database(new_note)

    def update_note(self, note_id, note):
        note_dict = self.translator.to_database(note)
        existing_note = Note.query.get(note_id)
        if existing_note:
            for key, value in note_dict.items():
                setattr(existing_note, key, value)
            db.session.commit()
            return self.translator.from_database(existing_note)

    def delete_note(self, note_id):
        existing_note = Note.query.get(note_id)
        if existing_note:
            db.session.delete(existing_note)
            db.session.commit()
