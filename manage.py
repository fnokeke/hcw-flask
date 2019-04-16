from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from hcw_flask import app
from hcw_flask.models import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(port=5500))

# app.run(threaded=True, debug=True, host='localhost', port=5500)

if __name__ == '__main__':
    manager.run()
