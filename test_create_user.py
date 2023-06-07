import pytest
from datetime import datetime
from config import db
from .app import app
from models import User

@pytest.fixture
def client():
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
    
    with app.app.test_client() as client:
        with app.app.app_context():
            db.create_all()
        yield client
        with app.app.app_context():
            db.drop_all()

def test_create_user(client):
    now = datetime.utcnow()
    new_user = {
        "fname": "Test",
        "lname": "User",
        "created_date": now
    }
    
    response = client.post("/users", json=new_user)
    json_data = response.get_json()
    print(json_data, flush=True)
    
    assert response.status_code == 200
    assert "id" in json_data
    assert json_data["fname"] == "Test"
    assert json_data["lname"] == "User"
    assert json_data["created_date"] == now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


    user = db.session.get(User, json_data["id"])
    assert user is not None


# from .app import app
# import pytest
# import json

# class TestPersonRoutes:

#     @pytest.fixture
#     def client(self):
#         with app.app.test_client() as client:
#             with app.app.app_context():
#                 yield client

#     def test_get_person(self, client):
#         response = client.get("/users/1")
#         assert response.status_code == 200

#     def test_create_person(self, client):
#         json_body = {
#             "lname": "Ajax",
#             "fname": "Space",
#         }
#         response = client.post("/users", data=json.dumps(json_body), content_type='application/json')
#         assert response.status_code == 200

#     def test_update_person(self, client):
#         json_body = {
#             "lname": "Gaga",
#             "fname": "Updated",
#         }
#         response = client.put("/users/7", data=json.dumps(json_body), content_type='application/json')
#         assert response.status_code == 200

#     def test_delete_person(self, client):
#         response = client.delete("/users/11")
#         assert response.status_code == 200
    
#     def test_person_invalid_id(self, client):
#         response = client.get("/users/182781")
#         error_message = response.json
#         assert error_message["detail"] == "The user id not found"
#         assert error_message["title"] == "Not Found"
#         assert response.status_code == 404


# class TestNotesRoutes:

#     @pytest.fixture
#     def client(self):
#         with app.app.test_client() as client:
#             with app.app.app_context():
#                 yield client

#     def test_get_one_note(self, client):
#         response = client.get("/users/7/notes/12")
#         assert response.status_code == 200

#     def test_create_note(self, client):
#         json_body = {
#             "content": "Darova",
#         }
#         response = client.post("/users/13/new", data=json.dumps(json_body), content_type='application/json')
#         assert response.status_code == 200

#     def test_update_note(self, client):
#         json_body = {
#             "content": "Updated Maliyan",
#         }
#         response = client.put("/users/12/notes/28", data=json.dumps(json_body), content_type='application/json')
#         assert response.status_code == 200

#     def test_delete_note(self, client):
#         response = client.delete("/users/7/notes/12")
#         assert response.status_code == 200

#     def test_note_invalid_id(self, client):
#         response = client.get("/users/7/notes/12754")
#         assert response.status_code == 404
