from django.urls import path
from django.conf import settings
from .views import EventsView
from django.conf.urls.static import static

urlpatterns = [
    path('', EventsView, name="events")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)