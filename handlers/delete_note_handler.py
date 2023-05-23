from handlers.base_handler import BaseHandler
from services.delete_note_service import DeleteNoteService

class DeleteNoteHandler(BaseHandler):
    def __init__(self):
        self.service = DeleteNoteService()

    def delete_note(self, note_id=None):
        return self.service.delete(note_id)
 