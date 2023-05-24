from repositories import NotesRepository
from infrastructure_exceptions import NotFoundException

class NotesService:
    def __init__(self, notes_repositoty):
        self.repository = notes_repositoty

    def get(self, note_id):
        note = self.repository.get_note(note_id)
        if not note:
            raise NotFoundException
        return note

    def create(self, note):
        return self.repository.create_note(note)

    def update(self, note_id, note):
        return self.repository.update_note(note_id, note)

    def delete(self, note_id):
        return self.repository.delete_note(note_id)

notes_repository = NotesRepository()
notes_service = NotesService(notes_repository)
