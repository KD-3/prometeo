from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50, verbose_name="Event Name", default='name')
    image = models.ImageField(upload_to="images/", default="images/logo.png", verbose_name="Cover Image")
    rulebook = models.FileField(upload_to="rulebooks/", null=True, verbose_name="Rulebook File")
    prize = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Prize Money (Rs.)", default=0)
    description = models.TextField(max_length=5000, null=True, verbose_name="Event Description")
    date = models.DateField(null=True, verbose_name="Event Date")
    time = models.TimeField(null=True, verbose_name="Event Time")
    venue = models.CharField(max_length=50, null=True, verbose_name="Event Venue")
    
