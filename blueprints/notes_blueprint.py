from flask import Blueprint, request

from structure import(
    get_note_handler, 
    create_note_handler, 
    update_note_handler, 
    delete_note_handler
)

notes_blueprint = Blueprint('notes', __name__)


@notes_blueprint.route("/<int:user_id>/new", methods=['POST'])
def create_new_note(user_id):
    handler = create_note_handler
    new_note = request.json
    content = {'user_id': user_id, 'content': new_note['content']}
    return handler.create_note(note=content)


@notes_blueprint.route("/<int:user_id>/<int:note_id>", methods=['GET'])
def get_one_note(user_id, note_id):
    handler = get_note_handler
    return handler.get_note(note_id=note_id)


@notes_blueprint.route("/<int:user_id>/<int:note_id>", methods=['PUT'])
def update_one_note(user_id, note_id):
    handler = update_note_handler
    content = request.json
    return handler.update_note(note_id=note_id, note=content)


@notes_blueprint.route("/<int:user_id>/<int:note_id>", methods=['DELETE'])
def delete_one_note(user_id, note_id):
    handler = delete_note_handler
    handler.delete_note(note_id=note_id)
    return 'Note deleted', 200
