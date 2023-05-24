from .app import app
import pytest
import json

class TestPersonRoutes:

    @pytest.fixture
    def client(self):
        with app.app.test_client() as client:
            with app.app.app_context():
                yield client

    def test_get_person(self, client):
        response = client.get("/users/1")
        assert response.status_code == 200

    def test_create_person(self, client):
        json_body = {
            "lname": "Ajax",
            "fname": "Space",
        }
        response = client.post("/users", data=json.dumps(json_body), content_type='application/json')
        assert response.status_code == 200

    def test_update_person(self, client):
        json_body = {
            "lname": "Gaga",
            "fname": "Updated",
        }
        response = client.put("/users/7", data=json.dumps(json_body), content_type='application/json')
        assert response.status_code == 200

    def test_delete_person(self, client):
        response = client.delete("/users/11")
        assert response.status_code == 200
    
    def test_person_invalid_id(self, client):
        response = client.get("/users/182781")
        error_message = response.json
        assert error_message["detail"] == "The user id not found"
        assert error_message["title"] == "Not Found"
        assert response.status_code == 404


class TestNotesRoutes:

    @pytest.fixture
    def client(self):
        with app.app.test_client() as client:
            with app.app.app_context():
                yield client

    def test_get_one_note(self, client):
        response = client.get("/users/7/notes/12")
        assert response.status_code == 200

    def test_create_note(self, client):
        json_body = {
            "content": "Darova",
        }
        response = client.post("/users/13/new", data=json.dumps(json_body), content_type='application/json')
        assert response.status_code == 200

    def test_update_note(self, client):
        json_body = {
            "content": "Updated Maliyan",
        }
        response = client.put("/users/12/notes/28", data=json.dumps(json_body), content_type='application/json')
        assert response.status_code == 200

    def test_delete_note(self, client):
        response = client.delete("/users/7/notes/12")
        assert response.status_code == 200

    def test_note_invalid_id(self, client):
        response = client.get("/users/7/notes/12754")
        assert response.status_code == 404
