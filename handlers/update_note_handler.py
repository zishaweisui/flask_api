from handlers.base_handler import BaseHandler
from services.update_note_service import UpdateNoteService

class UpdateNoteHandler(BaseHandler):
    def __init__(self):
        self.service = UpdateNoteService()

    def update_note(self, note_id=None, note=None):
        return self.service.update(note_id, note)
        