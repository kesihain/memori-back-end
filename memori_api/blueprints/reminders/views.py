from flask import Blueprint,jsonify,request
from models.location import Location
from models.reminder import Reminder
from models.user import User
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

reminders_api_blueprint = Blueprint('reminder_api',
                                __name__,
                                template_folder='templates')

@reminders_api_blueprint.route('/create',methods=['POST'])
@jwt_required
def create():
    location_id=request.json.get('location_id')
    item_name=request.json.get('item_name')
    location = Location.get_by_id(int(location_id))
    reminder = Reminder(location=location_id,item_name=item_name)
    if reminder.save():
        result={'id':reminder.id,'item':reminder.item_name,'location':location.name}
        return jsonify(result)
    else:
        result={'message':'Could not save reminder. Try again later'}

@reminders_api_blueprint.route('/show',methods=['GET'])
@jwt_required
def show():
    username=get_jwt_identity()
    user = User.get_or_none(User.username==username)
    result=[]
    for location in user.locations:
        for reminder in location.reminders:
            item = {'id':reminder.id,'item':reminder.item_name,'location':location.name}
            result.append(item)
    return jsonify(result)