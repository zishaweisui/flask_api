from flask import make_response
from config import db
from models import Note

class DeleteNoteRepository:
    def delete_note(self, note_id):
        existing_note = Note.query.get(note_id)
        if existing_note:
            db.session.delete(existing_note)
            db.session.commit()
            return make_response(f"{note_id} successfully deleted", 204)
