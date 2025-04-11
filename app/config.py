import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_FILE = os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_FILE}'
SQLALCHEMY_TRACK_MODIFICATIONS = False