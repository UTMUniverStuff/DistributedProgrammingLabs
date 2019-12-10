from enterprise.message_model import MessageModel


class MessageSender:
    def send_message(self, message_model: MessageModel):
        raise NotImplementedError()

