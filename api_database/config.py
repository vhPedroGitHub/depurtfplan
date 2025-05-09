# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://myuser:mypassword@db:5432/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False