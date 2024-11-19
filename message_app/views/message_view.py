class MessageView:
    @staticmethod
    def render_message(message):
        return {
            "message_id": message.message_id,
            "sender_id": message.sender_id,
            "recipient_id": message.recipient_id,
            "content": message.content,
            "created_at": message.created_at
        }

    @staticmethod
    def render_messages(messages):
        return [MessageView.render_message(msg) for msg in messages]