from flask import Flask
from config import app 

from blueprints import(
    users_blueprint,
    notes_blueprint
)

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(notes_blueprint, url_prefix='/notes')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
