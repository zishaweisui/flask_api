from flask import request
import config
from structure import (
    get_users_handler, 
    get_user_handler, 
    create_user_handler, 
    update_user_handler, 
    delete_user_handler,
    get_note_handler, 
    create_note_handler, 
    update_note_handler, 
    delete_note_handler
)

app = config.connex_app

@app.route("/users", methods=['GET'])
def home():
    handler = get_users_handler
    return handler.get_users()


@app.route("/users", methods=['POST'])
def create_user():
    handler = create_user_handler
    return handler.create_user()


@app.route("/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    handler = get_user_handler
    return handler.get_user(user_id=user_id)


@app.route("/users/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    handler = update_user_handler
    return handler.update_user(user_id=user_id)


@app.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    handler = delete_user_handler
    handler.delete_user(user_id=user_id)
    return 'User deleted', 200


@app.route("/users/<int:user_id>/notes/<int:note_id>", methods=['GET'])
def get_one_note(user_id, note_id):
    handler = get_note_handler
    return handler.get_note(note_id=note_id)


@app.route("/users/<int:user_id>/new", methods=['POST'])
def create_new_note(user_id):
    handler = create_note_handler
    new_note = request.json
    content = {'user_id': user_id, 'content': new_note['content']}
    return handler.create_note(note=content)


@app.route("/users/<int:user_id>/notes/<int:note_id>", methods=['PUT'])
def update_one_note(user_id, note_id):
    handler = update_note_handler
    content = request.json
    return handler.update_note(note_id=note_id, note=content)


@app.route("/users/<int:user_id>/notes/<int:note_id>", methods=['DELETE'])
def delete_one_note(user_id, note_id):
    handler = delete_note_handler
    handler.delete_note(note_id=note_id)
    return 'Note deleted', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
