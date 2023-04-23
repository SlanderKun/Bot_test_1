from app.models.User import User
from app import app
import json
from flask import jsonify, abort, request
from app.services.SecurityService import Security
from app.models.UsersEncoder import UsersEncoder


@app.route('/users', methods=['GET'])
def get_users():
    token = request.headers.get("Authorization")
    Security.authorization(token)
    users = User.query.all()
    json_users = []
    for user in users:
        json_users.append(user.to_dict())
    return jsonify(json_users)


@app.route('/users/<int:id>', methods=['GET'])
def find_user_by_id(id):
    token = request.headers.get("Authorization")
    Security.authorization(token)
    with app.app_context():
        user = User.query.filter_by(id=str(id)).first()
    if user != None:
        json_user = {
            'id': user.id,
            'username': user.username,
            'display_name': user.display_name,
            'is_active': user.is_active
        }
        return json.dumps(json_user)
    abort(404)


@app.route('/users/',)
def get_token():
    pass

