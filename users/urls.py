from django.urls import path
from .views import *

urlpatterns = [
    path('info', users_info, name='users_info'),
    path('<int:userid>/info', events_info, name='events_info'),
]
