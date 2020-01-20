from django.db import models

# Create your models here.
EVENT_CHOICES = (
    ('technical','Technical'),
    ('workshop','Workshop'),
    ('informal','Informal'),
)

EVENT_PARTICIPATION = (
    ('individual', 'Individual Event'),
    ('team', 'Team Event')
)

class Event(models.Model):
    name = models.CharField(max_length=50, verbose_name="Event Name", unique=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Cover Image")
    rulebook = models.FileField(upload_to="rulebooks/", null=True, blank=True, verbose_name="Rulebook File")
    participation_type = models.CharField(max_length=25,choices=EVENT_PARTICIPATION,default='team', verbose_name="Participation Type")
    min_team_size = models.IntegerField(verbose_name="Minimum Team Size (leave unchanged for individual event)", default=3)
    max_team_size = models.IntegerField(verbose_name="Maximum Team Size (leave unchanged for individual event)", default=5)
    prize = models.IntegerField(verbose_name="Prize Money (Rs.)", null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Event Description")
    problem_statement = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Problem Statement")
    rulebook_text = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Rulebook Text (HTML Format)")
    host = models.CharField(max_length=50, null=True, blank=True, verbose_name="Event Host")
    external_link = models.URLField(max_length=500, null=True, blank=True, verbose_name="External Link for Registration")
    date = models.DateField(verbose_name="Event Date")
    time = models.TimeField(null=True, blank=True, verbose_name="Event Time")
    venue = models.CharField(max_length=50, null=True, blank=True, verbose_name="Event Venue")
    type = models.CharField(max_length=15,choices=EVENT_CHOICES,default='event', verbose_name='Event Type')
    def __str__(self):
        return self.name

    
