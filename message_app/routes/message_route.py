from flask import Blueprint
from message_app.controllers.message_controller import MessageController

message_bp = Blueprint('message_bp', __name__)

@message_bp.route('/api/messages', methods=['POST'])
def send_message():
    return MessageController.send_message()

@message_bp.route('/api/messages/<int:user_id>', methods=['GET'])
def get_messages(user_id):
    return MessageController.get_messages(user_id)