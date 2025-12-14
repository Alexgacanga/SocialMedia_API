from django.contrib.auth.models import Permission
from django.template.context_processors import request
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.Permission):
    def has_permissions_or_not(self, request, views, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return self.author == self.user
