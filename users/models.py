from django.contrib.auth.models import AbstractUser
from django.db import models
from events.models import Event
import uuid

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)

YEAR_CHOICES = (
    ('first_year', 'First Year'),
    ('second_year', 'Second Year'),
    ('third_year', 'Third Year'),
    ('fourth_year', 'Fourth Year'),
    ('fifth_year', 'Fifth Year')
)

class CustomUser(AbstractUser):
    events = models.ManyToManyField(Event, blank=True, related_name="participants")
    # first_name = forms.CharField(max_length=50, verbose_name='First Name')
    # last_name = forms.CharField(max_length=50, verbose_name='Last Name')
    # join_referral = models.CharField(max_length=8, null=True, blank=True, verbose_name='Referral Code for Joining')
    referred_by = models.ForeignKey("self", on_delete=models.CASCADE, related_name='referred_users', null=True)
    invite_referral = models.CharField(max_length=8, unique=True, null=True, blank=True, verbose_name='Referral Code for Inviting')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='Gender', default='male')
    contact = models.CharField(max_length=10, verbose_name='Contact')
    current_year = models.CharField(max_length=20, choices=YEAR_CHOICES, verbose_name='Current Year of Study', default='first_year')
    college = models.CharField(max_length=60, verbose_name='College Name')
    city = models.CharField(max_length=40, verbose_name='City')
    ambassador = models.BooleanField(verbose_name='Campus Ambassador', default=False, blank=True)
    def __str__(self):
        return self.username

class Team(models.Model):
    id = models.CharField(max_length=9, primary_key=True, verbose_name='Team ID')
    name = models.CharField(max_length=50, verbose_name="Team Name", unique=True)
    leader = models.ForeignKey(CustomUser, blank=True, related_name="teams_created", on_delete=models.CASCADE)
    members = models.ManyToManyField(CustomUser, related_name="teams")
    event = models.ForeignKey(Event, blank=True, related_name="participating_teams", on_delete=models.CASCADE)
    def __str__(self):
        return self.name
