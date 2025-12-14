from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.template.context_processors import request
from rest_framework import permissions, status, viewsets
from SocialMedia_API.users.serializers import UserSerializer
from SocialMedia_API.social.models import Post
from SocialMedia_API.users.models import Follow



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    class_serializer = UserSerializer
    class_permissions = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail = True, methods = ['post'], class_permissions = [permissions.IsAuthenticated])
    def follow(self, request, pk=None):
        target_user = self.get_object()
        current_user = request.user

        if current_user == target_user:
            return Response({"Error": f"You CANNOT follow yourself !!!"}, status = status.HTTP404_BAD_REQUEST)
        follow_instance, created = Follow.objects.get_or_create(
            follower = current_user,
            following = target_user
        )
        if created:
            return Response({"status": f"You are now following {target_user.username}"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": f"You already follow {target_user.username}"}, status=status.HTTP_200_OK)
    
    action(detail=True,methods=['post'],class_permissions=permissions.IsAuthenticated)
    def unfollow(self, request, pk=None):
        target_user = self.get_object()
        follow_instance = Follow.objects.filter(follower = request.user, following = target_user)
        if follow_instance.exists:
            follow_instance.delete()
            return Response({"status": f"You unfollowed {target_user.username}"}, status=status.HTTP_200_OK)
        return Response({"Error": f"You're not following {target_user.username}"}, status=status.HTTP_400_BAD_REQUEST)