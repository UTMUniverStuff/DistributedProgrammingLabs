from django.contrib import admin

# Register your models here.
from msg_broker.models import TopicToAddress

admin.site.register(TopicToAddress)