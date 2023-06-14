from handlers.base_handler import BaseHandler

class DeleteNoteHandler(BaseHandler):
    def __init__(self, notes_handler):
        self.service = notes_handler

    def delete_note(self, note_id=None):
        return self.service.delete(note_id)
