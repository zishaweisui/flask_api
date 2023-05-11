from flask import render_template, request
import config
from models import Person, Note
from people import read_one, update, delete, create
from notes import update_note, create_note, delete_note

app = config.connex_app

@app.route("/people", methods=['GET'])
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

@app.route("/people", methods=['POST'])
def create_person():
    person = request.json
    people = create(person)
    return render_template("home.html", people=people)

@app.route("/people/<person_id>", methods=['GET'])
def get_person(person_id):
    user = read_one(int(person_id))
    people = [user]
    return render_template("person.html", people=people)

@app.route("/people/<person_id>", methods=['PUT'])
def update_person(person_id):
    person = request.json
    user = update(int(person_id), person)
    people = [user]
    return render_template("home.html", people=people)

@app.route("/people/<person_id>", methods=['DELETE'])
def delete_person(person_id):
    return delete(int(person_id))

@app.route("/people/<person_id>/notes/<note_id>", methods=['GET'])
def get_one_note(person_id, note_id):
    notes = Note.query.get(note_id)
    person = Person.query.filter(Person.id == person_id).one_or_none()
    return render_template("note.html", note=notes, person=person)

@app.route("/people/<person_id>/new", methods=['POST'])
def create_new_note(person_id):
    new_note = request.json
    person_attr = request.view_args
    content = {**person_attr, 'content': new_note}
    note = create_note(content)
    return render_template("home.html", note=note)

@app.route("/people/<person_id>/notes/<note_id>", methods=['PUT'])
def update_one_note(person_id, note_id):
    content = request.json
    post = update_note(int(note_id), content)
    note = [post]
    return render_template("note.html", note=note)

@app.route("/people/<person_id>/notes/<note_id>", methods=['DELETE'])
def delete_one_note(person_id, note_id):
    return delete_note(int(note_id))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
