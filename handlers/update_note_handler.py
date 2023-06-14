from handlers.base_handler import BaseHandler

class UpdateNoteHandler(BaseHandler):
    def __init__(self, notes_service):
        self.service = notes_service

    def update_note(self, note_id=None, note=None):
        return self.service.update(note_id, note)
        