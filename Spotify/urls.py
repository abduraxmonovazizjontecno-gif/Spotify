from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Spotify import settings

urlpatterns = [
    path('',include('apps.urls')),
    path('admin_page/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
