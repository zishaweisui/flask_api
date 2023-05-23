from handlers.base_handler import BaseHandler
from services.get_note_service import GetNoteService

class GetNoteHandler(BaseHandler):
    def __init__(self):
        self.service = GetNoteService()

    def get_note(self, note_id=None):
        return self.service.read_one(note_id) 
        