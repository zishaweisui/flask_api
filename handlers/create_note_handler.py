from handlers.base_handler import BaseHandler
from services.notes_service import NoteService

class CreateNoteHandler(BaseHandler):
    def __init__(self):
        self.service  = NoteService()

    def create_note(self, note=None):
        return self.service.create(note)
            