from typing import Iterable


class TopicToAddressRepository:
    def get_addresses_subscribed_to_topic(self, topic: str) -> Iterable[str]:
        raise NotImplementedError()

    def add_address_to_topic(self, topic: str, address: str):
        raise NotImplementedError()