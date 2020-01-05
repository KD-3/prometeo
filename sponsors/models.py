from django.db import models

# Create your models here.
class Sponsor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Sponsor Name", unique=True)
    image = models.ImageField(upload_to="sponsorimages/", null=True, blank=True, verbose_name="Cover Image")
    type = models.CharField(max_length=100, verbose_name="Sponsor Type")