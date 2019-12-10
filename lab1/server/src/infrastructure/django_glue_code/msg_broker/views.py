import json

from django.http import HttpResponse
from django.views import View

from adapters.dtos import MessageDto, SubscriptionDto
from adapters.messaging_service import MessagingService
from msg_broker.di.di import obj_graph


class SubscribeView(View):
    messaging_service = obj_graph().provide(MessagingService)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        topic = body['topic']
        address = body['address']

        dto = SubscriptionDto(topic=topic, address=address)
        self.messaging_service.subscribe_address_to_topic(dto)

        return HttpResponse(status=204)


class SendMessageView(View):
    messaging_service = obj_graph().provide(MessagingService)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        topic = body['topic']
        message = body['message']

        dto = MessageDto(topic=topic, content=message)
        self.messaging_service.send_message(dto)

        return HttpResponse(status=204)
