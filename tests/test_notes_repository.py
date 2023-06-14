import pytest
from datetime import datetime
from config import (
    db, basedir
)
from app import (
    app
)
import shutil

original_db_path = basedir / 'people.db'
backup_db_path = basedir / 'people_backup.db'

@pytest.fixture(scope='module')
def test_client():
    shutil.copyfile(original_db_path, backup_db_path)
    
    with app.app.test_client() as client:
        with app.app.app_context():
            db.create_all()
        yield client
        with app.app.app_context():
            db.drop_all()

    shutil.copyfile(backup_db_path, original_db_path)

def test_create_note(test_client):
    new_user = {
        "fname": "Test",
        "lname": "User"
    }
    
    response = test_client.post("/users", json=new_user)
    user_id = response.get_json()["id"]

    new_note = {
        "content": "This is a note."
    }

    response = test_client.post(f"/users/{user_id}/new", json=new_note)
    json_data = response.get_json()

    assert response.status_code == 200
    assert "id" in json_data
    assert json_data["content"] == "This is a note."

def test_update_note(test_client):
    new_user = {
        "fname": "Test",
        "lname": "User"
    }
    
    response = test_client.post("/users", json=new_user)
    user_id = response.get_json()["id"]

    new_note = {
        "content": "This is a note.",
        "created_date": datetime.utcnow()
    }

    response = test_client.post(f"/users/{user_id}/new", json=new_note)
    note_id = response.get_json()["id"]
    now = datetime.utcnow()

    updated_note = {
        "content": "This is an updated note.",
        "updated_date": now
    }
    response = test_client.put(f"/users/{user_id}/notes/{note_id}", json=updated_note)
    
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["content"] == "This is an updated note."
    assert datetime.strptime(json_data["updated_date"], "%Y-%m-%dT%H:%M:%S.%fZ") >= updated_note["updated_date"]

def test_delete_note(test_client):
    new_user = {
        "fname": "Test",
        "lname": "User"
    }
    
    response = test_client.post("/users", json=new_user)
    user_id = response.get_json()["id"]

    new_note = {
        "content": "This is a note."
    }

    response = test_client.post(f"/users/{user_id}/new", json=new_note)
    note_id = response.get_json()["id"]

    response = test_client.delete(f"/users/{user_id}/notes/{note_id}")

    assert response.status_code == 200
