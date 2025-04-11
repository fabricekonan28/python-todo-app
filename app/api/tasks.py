from flask import Blueprint, jsonify, request
from app.models import Task

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

# Dummy data for now (will be replaced with database interaction)
tasks = []
next_task_id = 1

@tasks_bp.route('', methods=['POST'])
def create_task():
    global next_task_id
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'message': 'Title is required'}), 400

    new_task = Task(
        id=next_task_id,
        title=data['title'],
        description=data.get('description'),
        due_date=data.get('due_date'),
        priority=data.get('priority'),
        is_done=False
    )
    tasks.append(new_task.to_dict())
    next_task_id += 1
    return jsonify(new_task.to_dict()), 201

@tasks_bp.route('', methods=['GET'])
def get_all_tasks():
    return jsonify(tasks)

@tasks_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({'message': 'Task not found'}), 404