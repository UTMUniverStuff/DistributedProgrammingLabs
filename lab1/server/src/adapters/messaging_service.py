from adapters.dtos import MessageDto, SubscriptionDto
from business.message_sender import MessageSender
from business.topic_to_address_repository import TopicToAddressRepository
from enterprise.message_model import MessageModel


class MessagingService:
    def __init__(
            self,
            message_sender: MessageSender,
            topic_to_address_repository: TopicToAddressRepository):

        self._message_sender = message_sender
        self._topic_to_address_repository = topic_to_address_repository

    def subscribe_address_to_topic(self, dto: SubscriptionDto):
        self._topic_to_address_repository\
            .add_address_to_topic(topic=dto.topic, address=dto.address)

    def send_message(self, dto: MessageDto):
        addresses = self\
            ._topic_to_address_repository\
            .get_addresses_subscribed_to_topic(topic=dto.topic)

        for address in addresses:
            message_model = MessageModel(
                address=address,
                topic=dto.topic,
                content=dto.content)
            self._message_sender.send_message(message_model)
