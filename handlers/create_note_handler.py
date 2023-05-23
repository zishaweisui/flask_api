from handlers.base_handler import BaseHandler
from services.create_note_service import CreateNoteService

class CreateNoteHandler(BaseHandler):
    def __init__(self):
        self.service  = CreateNoteService()

    def create_note(self, note=None):
        return self.service.create(note)
            