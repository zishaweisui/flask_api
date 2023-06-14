from handlers import (
    GetUsersHandler, GetUserHandler, CreateUserHandler, UpdateUserHandler, DeleteUserHandler,
    GetNoteHandler, CreateNoteHandler, UpdateNoteHandler, DeleteNoteHandler
)
from services import (
    users_service, notes_service
)

from presenters import (
    note_presenter, user_presenter
)

get_users_handler = GetUsersHandler(users_service, user_presenter)
get_user_handler = GetUserHandler(users_service, user_presenter)
create_user_handler = CreateUserHandler(users_service)
update_user_handler = UpdateUserHandler(users_service)
delete_user_handler = DeleteUserHandler(users_service)

get_note_handler = GetNoteHandler(notes_service, note_presenter)
create_note_handler = CreateNoteHandler(notes_service)
update_note_handler = UpdateNoteHandler(notes_service)
delete_note_handler = DeleteNoteHandler(notes_service)
