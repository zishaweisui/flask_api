from handlers.base_handler import BaseHandler

class GetNoteHandler(BaseHandler):
    def __init__(self, notes_service):
        self.service = notes_service

    def get_note(self, note_id=None):
        return self.execute(
            self.service.get,
            note_id
        )
        