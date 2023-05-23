from repositories.create_note_repo import CreateNoteRepository

class CreateNoteService:
    def __init__(self):
        self.repo = CreateNoteRepository()
    
    def create(self, note):
        return self.repo.create_note(note)
