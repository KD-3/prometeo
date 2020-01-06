from django.urls import path
from .views import *

urlpatterns = [
    path('info', users_info, name='users_info'),
    path('info/<int:userid>', user_info, name='user_info'),
    path('create-team', create_team, name='create_team'),
    path('join-team', join_team, name='join_team'),
    path('team-created/', team_created, name='team_created'),
]
