from typing import TypeVar, Optional

from pinject import BindingSpec
from pinject.object_graph import ObjectGraph, new_object_graph

from infrastructure.msg_sending_glue_code.message_sender import MessageSender
from msg_broker.di.di_imports import di_imports
from msg_broker.repositories.topic_to_address_repository import TopicToAddressRepository


class DjangoProjectBindingSpec(BindingSpec):
    def configure(self, bind):
        bind('message_sender', to_class=MessageSender)
        bind('topic_to_address_repository', to_class=TopicToAddressRepository)


class ObjectGraphWrapper:
    """A wrapper to allow typing"""

    T = TypeVar('T')

    def __init__(self, pinject_obj_graph: ObjectGraph):
        self._obj_graph = pinject_obj_graph

    def provide(self, cls: T) -> T:
        return self._obj_graph.provide(cls)


_obj_graph: Optional[ObjectGraphWrapper] = None


def obj_graph() -> ObjectGraphWrapper:
    global _obj_graph

    if _obj_graph is None:
        di_imports()
        pinject_obj_graph = new_object_graph(binding_specs=(DjangoProjectBindingSpec(),))
        _obj_graph = ObjectGraphWrapper(pinject_obj_graph)

    return _obj_graph
