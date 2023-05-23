from handlers.base_handler import BaseHandler
from services.notes_service import NoteService

class GetNoteHandler(BaseHandler):
    def __init__(self):
        self.service = NoteService()

    def get_note(self, note_id=None):
        return self.service.read_one(note_id) 
        