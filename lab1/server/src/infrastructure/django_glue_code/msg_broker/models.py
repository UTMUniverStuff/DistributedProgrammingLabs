from django.db import models


class TopicToAddress(models.Model):
    topic = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
