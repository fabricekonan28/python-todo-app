from flask import Blueprint, jsonify, request
from app.database import db, TaskModel

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_bp.route('', methods=['GET'])
def get_all_tasks():
    tasks = TaskModel.query.all()
    return jsonify([task.to_dict() for task in tasks])

@tasks_bp.route('', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Le titre est requis'}), 400

    new_task = TaskModel(title=data['title'], description=data.get('description'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@tasks_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = TaskModel.query.get_or_404(task_id)
    return jsonify(task.to_dict())

@tasks_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = TaskModel.query.get_or_404(task_id)
    data = request.get_json()
    if data:
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.due_date = data.get('due_date', task.due_date)
        task.priority = data.get('priority', task.priority)
        task.is_done = data.get('is_done', task.is_done)
        db.session.commit()
        return jsonify(task.to_dict())
    return jsonify({'error': 'Aucune donnée fournie pour la mise à jour'}), 400

@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = TaskModel.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Tâche supprimée'}), 204