from flask import Flask
from app.api.tasks import tasks_bp  # Importe le Blueprint des tâches

app = Flask(__name__)
app.register_blueprint(tasks_bp)  # Enregistre le Blueprint

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)