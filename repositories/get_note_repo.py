from models import Note, note_schema

class GetNoteRepository:
    def get_one_note(self, note_id):
        note = Note.query.get(note_id)
        if note is not None:
            return note_schema.dump(note)
