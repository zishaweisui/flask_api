from handlers.base_handler import BaseHandler

class CreateNoteHandler(BaseHandler):
    def __init__(self, notes_handler):
        self.service  = notes_handler

    def create_note(self, note=None):
        return self.service.create(note)
            