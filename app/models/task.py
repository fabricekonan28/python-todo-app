class Task:
    def __init__(self, id, title, description=None, due_date=None, priority=None, is_done=False):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.is_done = is_done

    def __repr__(self):
        return f"<Task id={self.id}, title='{self.title}', is_done={self.is_done}>"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority,
            'is_done': self.is_done
        }
        