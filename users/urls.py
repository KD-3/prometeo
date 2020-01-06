from django.urls import path
from .views import *

urlpatterns = [
    path('info', users_info, name='users_info'),
    path('info/<int:userid>', user_info, name='user_info'),
]
