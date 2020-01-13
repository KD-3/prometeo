from django.db import models

ROLES = (
    ('pr_team_member', 'PR Team Member'),
    ('coordinator', 'Coordinator'),
    ('workshop_coordinator', 'Workshop Coordinator'),
    ('technical_coordinator', 'Technical Event Coordinator'),
    ('informal_coordinator', 'Informal Event Coordinator'),
    ('webd_team_member', 'WebD Team Member'),
    
)

# Create your models here.
class Carousel(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True, verbose_name='Display Name')
    image = models.ImageField(upload_to='carousel_images/', verbose_name='Image to Display in Slide')

class Coordinator(models.Model):
    name = models.CharField(max_length=40, verbose_name="Name")
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name='Profile Image')
    role = models.CharField(max_length=30, choices=ROLES, default='pr_team_member', verbose_name='Role')
    instagram = models.URLField(blank=True, null=True, verbose_name='Instagram Handle')
    facebook = models.URLField(blank=True, null=True, verbose_name='Facebook Handle')
    github = models.URLField(blank=True, null=True, verbose_name='Github Handle')
    linkedin = models.URLField(blank=True, null=True, verbose_name='LinkedIn Handle')
    email = models.EmailField(max_length=100, blank=True, null=True, verbose_name='Email Address')
    designation = models.CharField(max_length=60, blank=True, null=True, verbose_name="Designation")
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name='About You')

