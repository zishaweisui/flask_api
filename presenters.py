class UserPresenter:
    def __init__(self, note_presenter):
        self.note_presenter = note_presenter

    def present(self, user):
        return {
            "id": user.id,
            "fname": user.fname,
            "lname": user.lname,
            "created_date": user.created_date,
            "updated_date": user.updated_date,
            "notes": [self.note_presenter.present(note) for note in user.notes],
        }

class NotePresenter:
    def present(self, note):
        return {
            "id": note.id,
            "user_id": note.user_id,
            "content": note.content,
            "created_date": note.created_date,
            "updated_date": note.updated_date,
        }

note_presenter = NotePresenter()
user_presenter = UserPresenter(note_presenter)
