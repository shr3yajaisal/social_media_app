from datetime import datetime
from shared.utils.db_utils import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255))
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    last_activity = db.Column(db.DateTime, default=datetime.utcnow)  
    status = db.Column(db.String(10), default="inactive") 

    def update_status(self):
        self.last_activity = datetime.utcnow()
        self.status = "active"
        db.session.commit()