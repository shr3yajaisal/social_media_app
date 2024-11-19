from shared.models.message_model import Message
from shared.utils.db_utils import db
from user_app.services.user_service import UserService


class MessageService:
    @staticmethod
    def send_message(sender_id, recipient_id, content):
        new_message = Message(sender_id=sender_id, recipient_id=recipient_id, content=content)
        db.session.add(new_message)
        db.session.commit()
        return new_message

    @staticmethod
    def get_messages(user_id):
        return Message.query.filter((Message.sender_id == user_id) | (Message.recipient_id == user_id)).all()
