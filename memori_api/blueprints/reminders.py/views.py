# from flask import Blueprint,jsonify,request
# from models.location import Location
# from models.reminder import Reminder
# from flask_jwt_extended import (
#     JWTManager, jwt_required, create_access_token,
#     get_jwt_identity
# )

# reminders_api_blueprint = Blueprint('reminder_api',
#                                 __name__,
#                                 template_folder='templates')

# @reminders_api_blueprint.route('/create',methods=['POST'])
# @jwt_required
# def create():
#     location_id=request.json.get