from flask import abort, make_response
from config import db
from models import Person, Note, note_schema

class NoteRepository:
    def get_all_notes(self):
        notes = Note.query.all()
        return note_schema.dump(notes)

    def get_one_note(self, note_id):
        note = Note.query.get(note_id)
        if note is not None:
            return note_schema.dump(note)

    def create_note(self, note):
        person_id = note.get("person_id")
        person = Person.query.get(person_id)

        if person:
            note_dict = note.get("content")
            note_dict["person_id"] = person_id
            new_note = note_schema.load(note_dict, session=db.session)
            db.session.add(new_note)
            db.session.commit()
            return note_schema.dump(new_note), 201

    def update_note(self, note_id, note):
        existing_note = Note.query.get(note_id)
        if existing_note:
            update_note = note_schema.load(note, session=db.session)
            existing_note.content = update_note.content
            db.session.merge(existing_note)
            db.session.commit()
            return note_schema.dump(existing_note), 201

    def delete_note(self, note_id):
        existing_note = Note.query.get(note_id)
        if existing_note:
            db.session.delete(existing_note)
            db.session.commit()
            return make_response(f"{note_id} successfully deleted", 204)
