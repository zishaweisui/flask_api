from flask import render_template, request
import config
from models import User
from handlers.get_users_handler import GetUsersHandler
from handlers.get_user_handler import GetUserHandler
from handlers.create_user_handler import CreateUserHandler
from handlers.update_user_handler import UpdateUserHandler
from handlers.delete_user_handler import DeleteUserHandler
from handlers.get_note_handler import GetNoteHandler
from handlers.create_note_handler import CreateNoteHandler
from handlers.update_note_handler import UpdateNoteHandler
from handlers.delete_note_handler import DeleteNoteHandler

app = config.connex_app

@app.route("/users", methods=['GET'])
def home():
    handler = GetUsersHandler()
    users = handler.get_users()
    return render_template("home.html", users=users)

@app.route("/users", methods=['POST'])
def create_user():
    handler = CreateUserHandler()
    users = handler.create_user()
    return render_template("home.html", users=users)

@app.route("/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    handler = GetUserHandler()
    user = handler.get_user(user_id=user_id)
    users = [user]
    return render_template("user.html", users=users)

@app.route("/users/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    handler = UpdateUserHandler()
    user = handler.update_user(user_id=user_id)
    users = [user]
    return render_template("home.html", users=users)

@app.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    handler = DeleteUserHandler()
    handler.delete_user(user_id=user_id)
    return 'User deleted', 200

@app.route("/users/<int:user_id>/notes/<int:note_id>", methods=['GET'])
def get_one_note(user_id, note_id):
    handler = GetNoteHandler()
    note = handler.get_note(note_id=note_id)
    user = User.query.filter(User.id == user_id).one_or_none()
    return render_template("note.html", note=note, user=user)

@app.route("/users/<int:user_id>/new", methods=['POST'])
def create_new_note(user_id):
    handler = CreateNoteHandler()
    new_note = request.json
    content = {'user_id': user_id, 'content': new_note}
    post = handler.create_note(note=content)
    return render_template("home.html", note=post)

@app.route("/users/<int:user_id>/notes/<int:note_id>", methods=['PUT'])
def update_one_note(user_id, note_id):
    handler = UpdateNoteHandler()
    content = request.json
    note = handler.update_note(note_id=note_id, note=content)
    return render_template("home.html", note=note)

@app.route("/users/<int:user_id>/notes/<int:note_id>", methods=['DELETE'])
def delete_one_note(user_id, note_id):
    handler = DeleteNoteHandler()
    handler.delete_note(note_id=note_id)
    return 'Note deleted', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
