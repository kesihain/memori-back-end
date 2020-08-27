from flask import Blueprint,jsonify,request
from models.location import Location
from models.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

locations_api_blueprint = Blueprint('location_api',
                                __name__,
                                template_folder='templates')

@locations_api_blueprint.route('/create',methods=['POST'])
@jwt_required
def create():
    name = request.json.get('name', None)
    full_address = request.json.get('address',None)
    username = get_jwt_identity()
    user = User.select().where(User.username==username)
    print(user[0])
    location = Location(name=name,full_address=full_address, user=user[0].id)
    if location.save():
        result = {'message':'Location created'}
        return jsonify(result)
    else:
        result={'message':'Failed to create location'}
        return jsonify(result)

@locations_api_blueprint.route('/show',methods=['GET'])
@jwt_required
def show():
    username = get_jwt_identity()
    user = User.get_or_none(User.username==username)
    # locations=[(item) for item in user.locations]
    # print(locations)
    # [locations.append(item) for item in user.locations]
    result=[]
    for location in user.locations:
        item = { 'id': 1, 'name': "Next Academy", 'latitude':3.1350424, 'longitude':101.6299529 }
        result.append(item)
        print(result)
    return jsonify(result)

