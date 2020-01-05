from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from home.views import home_redirect

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('accounts/', include('allauth.urls')),
    path('sponsors/', include('sponsors.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)