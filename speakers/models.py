from django.db import models

# Create your models here.
class Speaker(models.Model):
    name = models.CharField(max_length=50, verbose_name="Speaker Name")
    designation = models.CharField(max_length=200, null=True, blank=True, verbose_name="Designation")
    topic = models.CharField(max_length=70, verbose_name="Topic")
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Cover Image")
    description = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Description")
    profile_link = models.URLField(max_length=500, null=True, blank=True, verbose_name="Profile Link")
    date = models.DateField(verbose_name="Event Date")
    time = models.TimeField(null=True, blank=True, verbose_name="Event Time")
    venue = models.CharField(max_length=50, null=True, blank=True, verbose_name="Event Venue")

    def __str__(self):
        return self.name