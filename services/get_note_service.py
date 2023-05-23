from repositories.get_note_repo import GetNoteRepository

class GetNoteService:
    def __init__(self):
        self.repo = GetNoteRepository()
    
    def read_one(self, note_id):
        return self.repo.get_one_note(note_id)    
