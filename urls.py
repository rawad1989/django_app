from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
import users.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/v1/', include('apis.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('users/', include(users.urls))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
