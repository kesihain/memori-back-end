from flask import Blueprint,jsonify,request
from models.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


sessions_api_blueprint = Blueprint('sessions_api',
                                __name__,
                                template_folder='templates')

@sessions_api_blueprint.route('/',methods=['POST'])
def sessions():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username= request.json.get('username', None)
    password= request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    user=User.get_or_none(User.username==username)
    if user:
        valid_login=check_password_hash(user.password_hash,password)
        if valid_login:
            access_token = create_access_token(identity=username)
            result={
                "auth_token": access_token,
                "message": "Successfully signed in.",
                "status": "success",
                "user": {
                    "id": user.id,
                    "username": user.username
                }
            }
            return jsonify(result)
        else:
            return {
                "message": "Some error occurred. Please try again.",
                "status": "fail"
            }
    else:
        return {
            "message": "Some error occurred. Please try again.",
            "status": "fail"
        }