from django.urls import path
from .views import *

urlpatterns = [
    path('', events, name="events"),
    path('<int:eventid>/', event, name="event"),
    path('<int:eventid>/register', register_for_event, name='register'),
    path('registered',registered,name='registered'),
    path('<int:eventid>/registered_users', registered_users, name='registered_users'),
    path('workshops',workshops,name='workshops'),
    path('informals',informals,name='informals'),
    path('speakers',speakers,name='speakers'),
] 

