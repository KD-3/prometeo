from django.urls import path
from .views import *

urlpatterns = [
    path('users/<slug:username>/', user_info, name='user_info'),
    path('users/', users_info, name='users_info'),
]