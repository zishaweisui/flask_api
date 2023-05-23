from repositories.update_note_repo import UpdateNoteRepository

class UpdateNoteService:
    def __init__(self):
        self.repo = UpdateNoteRepository()
    
    def update(self, note_id, note):
        return self.repo.update_note(note_id, note)
