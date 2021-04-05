from django.urls import path
from users import views

urlpatterns = [
    path('list/', views.ListUsersView.as_view(), name='list_users'),
]
