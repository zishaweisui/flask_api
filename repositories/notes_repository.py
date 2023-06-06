from config import db
from models import Note, PlainNote

class NotesRepository:
    def __init__(self, note_translator):
        self.translator = note_translator

    def get_note(self, note_id):
        note = Note.query.get(note_id)
        if note is not None:
            return self.translator.from_database(note)
        return None

    def create_note(self, note: PlainNote):
        new_note = Note(**note)
        db.session.add(new_note)
        db.session.commit()
        return self.translator.from_database(new_note)

    def update_note(self, note_id, note:PlainNote):
        existing_note = Note.query.get(note_id)
        if existing_note:
            for key, value in note.items():
                setattr(existing_note, key, value)
            db.session.commit()
            return self.translator.from_database(existing_note)

    def delete_note(self, note_id):
        existing_note = Note.query.get(note_id)
        if existing_note:
            db.session.delete(existing_note)
            db.session.commit()
