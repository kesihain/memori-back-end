from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from memori_api.blueprints.users.views import users_api_blueprint
from memori_api.blueprints.sessions.views import sessions_api_blueprint
from memori_api.blueprints.locations.views import locations_api_blueprint
from memori_api.blueprints.reminders.views import reminders_api_blueprint

app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(sessions_api_blueprint, url_prefix= '/api/v1/login')
app.register_blueprint(locations_api_blueprint, url_prefix= '/api/v1/location')
app.register_blueprint(reminders_api_blueprint, url_prefix= '/api/v1/reminder')
