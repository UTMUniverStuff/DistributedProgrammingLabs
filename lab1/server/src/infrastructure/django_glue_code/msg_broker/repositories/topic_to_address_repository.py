from typing import Iterable

import business
from msg_broker.models import TopicToAddress


class TopicToAddressRepository(business.TopicToAddressRepository):
    def add_address_to_topic(self, topic: str, address: str):
        """Adds address to topic, if not subscribed to it already"""

        topic_to_addr = TopicToAddress.objects.all().filter(topic=topic)
        if address in (model.address for model in topic_to_addr):
            return

        model = TopicToAddress(topic=topic, address=address)
        model.save()

    def get_addresses_subscribed_to_topic(self, topic: str) -> Iterable[str]:
        topic_to_addr = TopicToAddress.objects.all().filter(topic=topic)
        return (model.address for model in topic_to_addr)
