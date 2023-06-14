from flask_script import Manager
from flask_migrate import MigrateCommand
import config

app = config.connex_app
db = config.db

manager = Manager(app.app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
