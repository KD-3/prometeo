from django.urls import path
from .views import EventsView

urlpatterns = [
    path('', EventsView, name="events")
] 

