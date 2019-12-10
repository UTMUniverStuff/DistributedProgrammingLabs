class MessageModel:
    def __init__(self, *, address: str, topic: str, content: str):
        self.address = address
        self.topic = topic
        self.content = content
