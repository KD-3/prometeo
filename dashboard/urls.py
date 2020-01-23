from django.urls import path
from .views import *

urlpatterns = [
    path('users/<int:userid>/', user_info, name='user_info'),
    path('users/', users_info, name='users_info'),
    path('events/', events_info, name='events_info'),
    path('events/<slug:type>/', event_type_info, name='event_type_info'),
    path('events/<slug:type>/<int:eventid>/', event_info, name='event_info'),
]