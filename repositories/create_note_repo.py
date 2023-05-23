from config import db
from models import User, note_schema

class CreateNoteRepository:
    def create_note(self, note):
        user_id = note.get("user_id")
        user = User.query.get(user_id)

        if user:
            note_dict = note.get("content")
            note_dict["user_id"] = user_id
            new_note = note_schema.load(note_dict, session=db.session)
            db.session.add(new_note)
            db.session.commit()
            return note_schema.dump(new_note), 201
