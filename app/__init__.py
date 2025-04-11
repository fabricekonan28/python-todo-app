from flask import Flask

app = Flask(__name__)
app.config.from_object('app.config')

from .api.tasks import tasks_bp
app.register_blueprint(tasks_bp)

from .database import init_db

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')