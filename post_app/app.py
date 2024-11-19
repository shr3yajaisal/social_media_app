import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from post_app.routes.post_routes import post_bp
from shared.utils.db_utils import db
from message_app.routes.message_route import message_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost:3306/social_media_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

@app.route('/')
def index():
    return "post app is running"

app.register_blueprint(post_bp)
app.register_blueprint(message_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
