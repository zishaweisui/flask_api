from handlers.base_handler import BaseHandler
from services.notes_service import NoteService

class DeleteNoteHandler(BaseHandler):
    def __init__(self):
        self.service = NoteService()

    def delete_note(self, note_id=None):
        return self.service.delete(note_id)
 