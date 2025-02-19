from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('data.urls')),
    path('', include('users.urls')),
    #path('users/', include('users.urls')),
    #path('data/', include('data.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)