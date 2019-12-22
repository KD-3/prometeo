from django.db import models

# Create your models here.
class Carousel(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True, verbose_name='Display Name')
    image = models.ImageField(upload_to='carousel_images/', verbose_name='Image to Display in Slide')
