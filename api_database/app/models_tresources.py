# app/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class T_Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(80), unique=True, nullable=False)
    resource_type = db.Column(db.String(120), unique=True, nullable=False)
    state_resource = db.Column(db.String(128), nullable=False)
    id_users = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Resource {self.resource_name}>'

    def serialize(self):
        return {
            'id': self.id,
            'resource_name': self.resource_name,
            'resource_type': self.resource_type,
            'state_resource': self.state_resource,
            'id_users': self.id_users,
        }