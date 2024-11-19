from shared.models.user_model import User
from shared.utils.db_utils import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

class UserService:
    @staticmethod
    def create_user(username, email, password, full_name, bio):
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password, full_name=full_name, bio=bio)
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def verify_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None

    @staticmethod
    def check_user_status(user):
        if user.last_activity < datetime.utcnow() - timedelta(minutes=10):  
            user.status = "inactive"
            db.session.commit()
        else:
            user.status = "active"
            db.session.commit()
