from django.contrib.auth.models import AbstractUser
from django.db import models
from events.models import Event

class CustomUser(AbstractUser):
    events = models.ManyToManyField(Event, blank=True, related_name="participants")
    def __str__(self):
        return self.username