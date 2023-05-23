from handlers.base_handler import BaseHandler
from services.notes_service import NoteService

class UpdateNoteHandler(BaseHandler):
    def __init__(self):
        self.service = NoteService()

    def update_note(self, note_id=None, note=None):
        return self.service.update(note_id, note)
        