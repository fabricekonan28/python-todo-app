from . import db
from sqlalchemy import Column, Integer, String, Text, Date, Boolean

class TaskModel(db.Model):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    due_date = Column(Date)
    priority = Column(String(20))
    is_done = Column(Boolean, default=False)

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