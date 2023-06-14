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

def test_create_user(test_client):
    now = datetime.utcnow()
    print(type(now), flush=True)
    new_user = {
        "fname": "Test",
        "lname": "User",
        "created_date": now
    }
    
    response = test_client.post("/users", json=new_user)
    json_data = response.get_json()
    print(json_data, flush=True)
    
    assert response.status_code == 200
    assert "id" in json_data
    assert json_data["fname"] == "Test"
    assert json_data["lname"] == "User"
    assert json_data["created_date"] == now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

def test_update_user(test_client):
    now = datetime.utcnow()
    new_user = {
        "fname": "Test",
        "lname": "User",
        "created_date": now
    }
    
    response = test_client.post("/users", json=new_user)
    user_id = response.get_json()["id"]

    updated_user = {
        "fname": "Updated",
        "lname": "User",
        "updated_date": now
    }
    response = test_client.put(f"/users/{user_id}", json=updated_user)
    
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["fname"] == "Updated"
    assert json_data["lname"] == "User"
    assert datetime.strptime(json_data["updated_date"], "%Y-%m-%dT%H:%M:%S.%fZ") >= updated_user["updated_date"]

def test_delete_user(test_client):
    now = datetime.utcnow()
    new_user = {
        "fname": "Test",
        "lname": "User",
        "created_date": now
    }
    
    response = test_client.post("/users", json=new_user)
    user_id = response.get_json()["id"]

    response = test_client.delete(f"/users/{user_id}")

    assert response.status_code == 200
