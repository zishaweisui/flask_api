from repositories.notes_repository import NoteRepository

class NoteService:
    def __init__(self):
        self.repo = NoteRepository()

    def read_all(self):
        return self.repo.get_all_notes()

    def read_one(self, note_id):
        return self.repo.get_one_note(note_id)

    def create(self, note):
        return self.repo.create_note(note)

    def update(self, note_id, note):
        return self.repo.update_note(note_id, note)

    def delete(self, note_id):
        return self.repo.delete_note(note_id)
