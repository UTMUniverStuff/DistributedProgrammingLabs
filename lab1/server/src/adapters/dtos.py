class MessageDto:
    def __init__(self, *, topic: str, content: str):
        self.topic = topic
        self.content = content


class SubscriptionDto:
    def __init__(self, *, topic: str, address: str):
        self.topic = topic
        self.address = address
