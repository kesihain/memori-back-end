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
    latitude = request.json.get('latitude',None)
    longitude = request.json.get('longitude',None)
    username = get_jwt_identity()
    user = User.get_or_none(User.username==username)
    # print(user[0])
    location = Location(name=name,full_address=full_address, user=user.id)
    if (latitude!=None and longitude!=None):
        location = Location(name=name,full_address=full_address, user=user.id, longitude=longitude,latitude=latitude)
    if location.save():
        result = {
            'id':location.id,'name':name,'address':full_address,'longitude':longitude,'latitude':latitude
        }
        return jsonify(result)
    else:
        result={'message':'Failed to create location'}
        return jsonify(result)

@locations_api_blueprint.route('/show',methods=['GET'])
@jwt_required
def show():
    username = get_jwt_identity()
    user = User.get_or_none(User.username==username)
    result=[]
    for location in user.locations:
        item = { 'id': location.id, 'name':location.name, 'latitude':location.latitude, 'longitude':location.longitude }
        result.append(item)
    return jsonify(result)

