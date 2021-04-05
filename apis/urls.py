from django.urls import path
from django.conf.urls import include
from apis.user.views import api_urls as user_urls

urlpatterns = [
    path('user/', include(user_urls)),
]
