from flask import render_template, request
import config
from models import User
from handlers.user_handler import UserHandler
from handlers.notes_handler import NotesHandler

app = config.connex_app
user_handler = UserHandler()
notes_handler = NotesHandler()

@app.route("/users", methods=['GET'])
def home():
    users = user_handler.routes()
    return render_template("home.html", users=users)

@app.route("/users", methods=['POST'])
def create_user():
    users = user_handler.routes()
    return render_template("home.html", users=users)

@app.route("/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    user = user_handler.routes(user_id=user_id)
    users = [user]
    return render_template("user.html", users=users)

@app.route("/users/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    user = user_handler.routes(user_id=user_id)
    users = [user]
    return render_template("home.html", users=users)

@app.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    user_handler.routes(user_id=user_id)
    return 'User deleted', 200

@app.route("/users/<int:user_id>/notes/<int:note_id>", methods=['GET'])
def get_one_note(user_id, note_id):
    note = notes_handler.routes(note_id=note_id)
    user = User.query.filter(User.id == user_id).one_or_none()
    return render_template("note.html", note=note, user=user)

@app.route("/users/<int:user_id>/new", methods=['POST'])
def create_new_note(user_id):
    new_note = request.json
    content = {'user_id': user_id, 'content': new_note}
    post = notes_handler.routes(note=content)
    return render_template("home.html", note=post)

@app.route("/users/<int:user_id>/notes/<int:note_id>", methods=['PUT'])
def update_one_note(user_id, note_id):
    content = request.json
    note = notes_handler.routes(note_id=note_id, note=content)
    return render_template("home.html", note=note)

@app.route("/users/<int:user_id>/notes/<int:note_id>", methods=['DELETE'])
def delete_one_note(user_id, note_id):
    notes_handler.routes(note_id=note_id)
    return 'Note deleted', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
