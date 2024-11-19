from flask import request, jsonify
from message_app.services.message_service import MessageService
from message_app.views.message_view import MessageView

class MessageController:
    @staticmethod
    def send_message():
        data = request.get_json()
        sender_id = data.get('sender_id')
        recipient_id = data.get('recipient_id')
        content = data.get('content')

        message = MessageService.send_message(sender_id, recipient_id, content)
        return MessageView.render_message(message), 201

    @staticmethod
    def get_messages(user_id):
        messages = MessageService.get_messages(user_id)
        return MessageView.render_messages(messages), 200