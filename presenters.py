class UserPresenter:
    def __init__(self, note_presenter):
        self.note_presenter = note_presenter

    def present(self, user):
        return {
            "id": user.id,
            "fname": user.fname,
            "lname": user.lname,
            "timestamp": user.timestamp,
            "notes": [self.note_presenter.present(note) for note in user.notes],
        }

class NotePresenter:
    def present(self, note):
        return {
            "id": note.id,
            "user_id": note.user_id,
            "content": note.content,
            "timestamp": note.timestamp,
        }

note_presenter = NotePresenter()
user_presenter = UserPresenter(note_presenter)
