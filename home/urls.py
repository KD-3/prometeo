from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('', home, name='home'),
] 
