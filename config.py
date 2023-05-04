import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

basedir = pathlib.Path(__file__).parent.resolve()
# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Configure the SQLAlchemy part of the app instance
app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'people.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)
# Initialize Marshmallow
ma = Marshmallow(app)
migrate = Migrate(app, db)
