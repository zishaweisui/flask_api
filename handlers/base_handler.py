from flask import jsonify 
from ..exceptions import UserNotFoundError, NoteNotFoundError

class BaseHandler:
    def execute(self, *args, **kwargs):
        try: 
            data = self._execute(*args, **kwargs)
            return jsonify(data), 200
        except UserNotFoundError:
            response = {'error': 'User ID not found'}
            return jsonify(response), 404
        except NoteNotFoundError:
            response = {'error': 'Note ID not found'}
            return jsonify(response), 404
        except Exception:
            response = {'error': "Fuck you it's 500"}
            return jsonify(response), 500
