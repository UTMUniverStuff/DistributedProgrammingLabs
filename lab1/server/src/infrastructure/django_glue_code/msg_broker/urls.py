from django.urls import path

from msg_broker.views import SubscribeView, SendMessageView

urlpatterns = [
    path('subscribe', SubscribeView.as_view()),
    path('send_message', SendMessageView.as_view()),
]
