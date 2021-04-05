from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
import users.models
from django.core.cache import cache


class ListUsersView(ListView, PermissionRequiredMixin):
    template_name = 'list.html'
    queryset = users.models.User.objects.all()
    context_object_name = 'users'
    model = users.models.User

    def get_queryset(self):
        cache_key = 'users'

        if cache_key in cache:
            return cache.get(cache_key)

        cache.set(cache_key, self.queryset)
        return self.queryset
