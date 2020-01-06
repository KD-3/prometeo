from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:type>/', events, name="events"),
    path('<slug:type>/<int:eventid>/', event, name="event"),
    path('<int:eventid>/register/', register_for_event, name='register'),
    path('registered/',registered,name='registered'),
    path('speakers/',speakers,name='speakers'),
] 

