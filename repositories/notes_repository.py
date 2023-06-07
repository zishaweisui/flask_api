from config import db
from models import Note

class NotesRepository:
    def __init__(self, note_translator):
        self.translator = note_translator

    def get_note(self, note_id):
        note = Note.query.get(note_id)
        if note is not None:
            return note
        return None

    def create_note(self, plain_note):
        note = self.translator.to_database(plain_note)
        new_note = Note(**note)
        db.session.add(new_note)
        db.session.commit()
        return self.translator.from_database(new_note)

    def update_note(self, note_id, plain_note):
        note = self.translator.to_database(plain_note)
        new_note = {'content': note.get('content')}
        existing_note = Note.query.get(note_id)
        if existing_note:
            for key, value in new_note.items():
                setattr(existing_note, key, value)
            db.session.commit()
            return self.translator.from_database(existing_note)

    def delete_note(self, note_id):
        existing_note = Note.query.get(note_id)
        if existing_note:
            db.session.delete(existing_note)
            db.session.commit()
