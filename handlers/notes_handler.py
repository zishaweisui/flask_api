from flask import request
from .exceptions import NoteNotFoundError
from handlers.base_handler import BaseHandler
from services.notes_service import NoteService

class NotesHandler(BaseHandler):
    def __init__(self):
        self.service = NoteService()

    def routes(self, note_id=None, note=None):
        if request.method == 'GET':
            if note_id:
                return self.service.read_one(note_id)  
            else: 
                return self.service.read_all()
        elif request.method == 'POST':
            return self.service.create(note)
        elif request.method == 'PUT':
            return self.service.update(note_id, note)
        elif request.method == 'DELETE':
            return self.service.delete(note_id)
        else:
            raise NoteNotFoundError
    