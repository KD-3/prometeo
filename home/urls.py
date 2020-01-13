from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('team', team, name='team'),
    path('industry_day', industry_day, name='industry_day'),
] 
