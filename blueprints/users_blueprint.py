from flask import Blueprint

from structure import (
    get_users_handler, 
    get_user_handler, 
    create_user_handler, 
    update_user_handler, 
    delete_user_handler
)

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route("/", methods=['GET'])
def get_users():
    handler = get_users_handler
    return handler.get_users()


@users_blueprint.route("/", methods=['POST'])
def create_user():
    handler = create_user_handler
    return handler.create_user()


@users_blueprint.route("/<int:user_id>", methods=['GET'])
def get_user(user_id):
    handler = get_user_handler
    return handler.get_user(user_id=user_id)


@users_blueprint.route("/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    handler = update_user_handler
    return handler.update_user(user_id=user_id)


@users_blueprint.route("/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    handler = delete_user_handler
    handler.delete_user(user_id=user_id)
    return 'User deleted', 200
