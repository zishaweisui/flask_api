from config import db
from models import Note, note_schema

class UpdateNoteRepository:
    def update_note(self, note_id, note):
        existing_note = Note.query.get(note_id)
        if existing_note:
            update_note = note_schema.load(note, session=db.session)
            existing_note.content = update_note.content
            db.session.merge(existing_note)
            db.session.commit()
            return note_schema.dump(existing_note), 201
