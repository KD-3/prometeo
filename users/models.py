from django.contrib.auth.models import AbstractUser
from django.db import models
from events.models import Event
import uuid

class CustomUser(AbstractUser):
    events = models.ManyToManyField(Event, blank=True, related_name="participants")
    def __str__(self):
        return self.username

class Team(models.Model):
    id = models.CharField(max_length=9, primary_key=True, verbose_name='Team ID')
    name = models.CharField(max_length=50, verbose_name="Team Name", unique=True)
    leader = models.ForeignKey(CustomUser, blank=True, related_name="teams_created", on_delete=models.CASCADE)
    members = models.ManyToManyField(CustomUser, related_name="teams")
    events = models.ManyToManyField(Event, blank=True, related_name="participating_teams")
    def __str__(self):
        return self.name