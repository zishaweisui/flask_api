from flask import render_template, request
import config
from models import Person
from handlers.people_handler import PeopleHandler
from handlers.notes_handler import NotesHandler

app = config.connex_app
people_handler = PeopleHandler()
notes_handler = NotesHandler()

@app.route("/people", methods=['GET'])
def home():
    people = people_handler.routes()
    return render_template("home.html", people=people)

@app.route("/people", methods=['POST'])
def create_person():
    people = people_handler.routes()
    return render_template("home.html", people=people)

@app.route("/people/<int:person_id>", methods=['GET'])
def get_person(person_id):
    user = people_handler.routes(person_id=person_id)
    people = [user]
    return render_template("person.html", people=people)

@app.route("/people/<int:person_id>", methods=['PUT'])
def update_person(person_id):
    user = people_handler.routes(person_id=person_id)
    people = [user]
    return render_template("home.html", people=people)

@app.route("/people/<int:person_id>", methods=['DELETE'])
def delete_person(person_id):
    people_handler.routes(person_id=person_id)
    return 'User deleted', 200

@app.route("/people/<int:person_id>/notes/<int:note_id>", methods=['GET'])
def get_one_note(person_id, note_id):
    note = notes_handler.routes(note_id=note_id)
    person = Person.query.filter(Person.id == person_id).one_or_none()
    return render_template("note.html", note=note, person=person)

@app.route("/people/<int:person_id>/new", methods=['POST'])
def create_new_note(person_id):
    new_note = request.json
    content = {'person_id': person_id, 'content': new_note}
    post = notes_handler.routes(note=content)
    return render_template("home.html", note=post)

@app.route("/people/<int:person_id>/notes/<int:note_id>", methods=['PUT'])
def update_one_note(person_id, note_id):
    content = request.json
    note = notes_handler.routes(note_id=note_id, note=content)
    return render_template("home.html", note=note)

@app.route("/people/<int:person_id>/notes/<int:note_id>", methods=['DELETE'])
def delete_one_note(person_id, note_id):
    notes_handler.routes(note_id=note_id)
    return 'Note deleted', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
