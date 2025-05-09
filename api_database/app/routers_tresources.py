# app/routes.py
from flask import jsonify, request
from app import app
from api_database.app.models_users import db
from api_database.app.models_tresources import T_Resource

@app.route('/resources', methods=['GET'])
def get_resources():
    resources = T_Resource.query.all()
    return jsonify([resource.serialize() for resource in resources])

@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = T_Resource.query.get_or_404(resource_id)
    return jsonify(resource.serialize())

@app.route('/resources', methods=['POST'])
def create_resource():
    data = request.get_json()
    new_resource = T_Resource(
        resource_name=data['resource_name'],
        resource_type=data['resource_type'],
        state_resource=data['state_resource'],
        id_users=data['id_users']
    )
    db.session.add(new_resource)
    db.session.commit()
    return jsonify(new_resource.serialize()), 201

@app.route('/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    resource = T_Resource.query.get_or_404(resource_id)
    data = request.get_json()
    resource.resource_name = data.get('resource_name', resource.resource_name)
    resource.resource_type = data.get('resource_type', resource.resource_type)
    resource.state_resource = data.get('state_resource', resource.state_resource)
    resource.id_users = data.get('id_users', resource.id_users)
    db.session.commit()
    return jsonify(resource.serialize())

@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    resource = T_Resource.query.get_or_404(resource_id)
    db.session.delete(resource)
    db.session.commit()
    return jsonify({'message': 'Resource deleted'})