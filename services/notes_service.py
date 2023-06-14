from repositories import NotesRepository
from translators import NoteTranslator
from infrastructure_exceptions import NotFoundException
from models import PlainNote

class NotesService:
    def __init__(self, notes_repository):
        self.repository = notes_repository

    def get(self, note_id):
        note = self.repository.get_note(note_id)
        if not note:
            raise NotFoundException
        return note

    def create(self, attributes):
        note = PlainNote(**attributes)
        # note["created_date"] = datetime.utcnow()-timedelta(days=30)
        return self.repository.create_note(note)

    def update(self, note_id, attributes):
        note = PlainNote(**attributes)
        return self.repository.update_note(note_id, note)

    def delete(self, note_id):
        return self.repository.delete_note(note_id)

note_translator = NoteTranslator()
notes_repository = NotesRepository(note_translator)
notes_service = NotesService(notes_repository)
