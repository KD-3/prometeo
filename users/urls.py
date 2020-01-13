from django.urls import path
from .views import *

urlpatterns = [
    path('info/', users_info, name='users_info'),
    path('info/<int:userid>/', user_info, name='user_info'),
    path('create_team/<int:eventid>/', create_team, name='create_team'),
    path('join_team/', join_team, name='join_team'),
    path('team_created/', team_created, name='team_created'),
    path('join_team/confirm/', join_team_confirm, name='join_team_confirm'),
    
]
