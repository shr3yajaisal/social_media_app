from flask import Flask
from shared.utils.db_utils import db
from shared.utils.db_utils import migrate
# from config.config import Config

# Initialize the Flask App
app = Flask(__name__)

# Initialization configuration
# (later move this configuration to config/config.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost:3306/social_media_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

from shared.models import user_model
from shared.models import post_model
from shared.models import message_model