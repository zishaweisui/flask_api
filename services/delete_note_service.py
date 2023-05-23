from repositories.delete_note_repo import DeleteNoteRepository

class DeleteNoteService:
    def __init__(self):
        self.repo = DeleteNoteRepository()

    def delete(self, note_id):
        return self.repo.delete_note(note_id)
