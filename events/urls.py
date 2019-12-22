from django.urls import path
from .views import *

urlpatterns = [
    path('', events, name="events"),
    path('<int:eventid>/', event, name="event"),
    path('<int:eventid>/register', register_for_event, name='register'),
] 

