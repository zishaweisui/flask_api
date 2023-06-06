class UserTranslator:
    def __init__(self, note_translator):
        self.note_translator = note_translator

    def to_database(self, user):
        return {
            "id": user.get("id"),
            "fname": user.get("fname"),
            "lname": user.get("lname"),
            "timestamp": user.get("timestamp"),
        }


    def from_database(self, user):
        return {
            "id": user.id,
            "fname": user.fname,
            "lname": user.lname,
            "timestamp": user.timestamp,
            "notes": [self.note_translator.from_database(note) for note in user.notes],
        }
        


class NoteTranslator:
    def to_database(self, note):
        return {
            "id": note.get("id"),
            "user_id": note.get("user_id"),
            "content": note.get("content"),
            "timestamp": note.get("timestamp"),
        }

    def from_database(self, note):
        return {
            "id": note.id,
            "user_id": note.user_id,
            "content": note.content,
            "timestamp": note.timestamp,
        }

# class UserTranslator:
#     def __init__(self, note_translator):
#         self.note_translator = note_translator

#     def to_database(self, user):
#         return {
#             "id": user.get("id"),
#             "fname": user.get("fname"),
#             "lname": user.get("lname"),
#             "timestamp": user.get("timestamp"),
#             "notes": [self.note_translator.to_database(note) for note in user.get("notes")],
#         }

# class NoteTranslator:
#     def to_database(self, note):
#         return {
#             "id": note.get("id"),
#             "user_id": note.get("user_id"),
#             "content": note.get("content"),
#             "timestamp": note.get("timestamp"),
#         }
