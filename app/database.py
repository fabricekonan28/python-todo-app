from flask_sqlalchemy import SQLAlchemy
from . import app  # Import l'instance 'app' créée dans __init__.py

db = SQLAlchemy(app)

class TaskModel(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.Date)
    priority = db.Column(db.String(20))
    is_done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task id={self.id}, title='{self.title}', is_done={self.is_done}>"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'priority': self.priority,
            'is_done': self.is_done
        }

def init_db():
    with app.app_context():
        db.create_all()