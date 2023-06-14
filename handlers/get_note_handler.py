from handlers.base_handler import BaseHandler

class GetNoteHandler(BaseHandler):
    def __init__(self, notes_service, presenter):
        super().__init__(presenter)
        self.service = notes_service

    def get_note(self, **kwargs):
        return self.execute(
            self.service.get,
            kwargs['note_id']
        )
        