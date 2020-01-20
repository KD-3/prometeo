from django.urls import path
from .views import *

urlpatterns = [
    path('registered/',registered,name='registered'),
    path('<slug:type>/', events, name="events"),
    path('<slug:type>/<int:eventid>/', event, name="event"),
    path('<int:eventid>/register/', register_for_event, name='register'),
] 

