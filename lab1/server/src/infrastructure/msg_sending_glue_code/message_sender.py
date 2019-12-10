import business
import requests

from enterprise.message_model import MessageModel


class MessageSender(business.MessageSender):
    def send_message(self, message_model: MessageModel):
        post_data = {
            'topic': message_model.topic,
            'content': message_model.content
        }

        requests.post(message_model.address, post_data)
