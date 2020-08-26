from flask import Blueprint,jsonify,request
from models.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('/', methods=['GET'])
def index():
    return "USERS API"

@users_api_blueprint.route('/signup/', methods=['POST'])
def create():
    username = request.json.get('username')
    email = request.json.get('email')
    # if  not ( User.get_or_none(User.username == username) or len(username)<0):
    new_user = User(username=username,email=email,password=request.json.get('password'))
    if new_user.save():
        result = "Successful sign up"
        return jsonify(result)
    else:
        result = []
        [result.append(error) for error in new_user.errors]
        return jsonify(result)