from django.contrib.auth import get_user_model
from django.forms import fields
from rest_framework.fields import ReadOnlyField, SlugField
from .models import User
from django.contrib.auth.decorators import user_passes_test
from rest_framework import serializers
from .models import Follow


User = get_user_model()

class UserSerializer(serializers.Serializer):
    password = serializers.CharField(write_only= True)
    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = {'email','bio','profile_picture','username','password','follower_count','following_count','id'}
        read_only_field = [id]

    def get_follower_count(self, obj):
        return obj.followers.count()
    
    def get_following_count(self,obj):
        return obj.following.count()
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password= validated_data['password'],
            profile_picture = validated_data.get('profile_picture', None),
            bio = validated_data.get('bio', ''),
        )
        return user

class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source = 'follower.username')
    following = serializers.SlugRelatedField(
        slug_field = 'username',
        queryset = User.objects.all()
    )
    class Meta:
        model = Follow
        fields = ['follower', 'following','created_at','id']
    def validate(self, data):
       if self.context['request'].user == data['following']:
           raise serializers.ValidationError("You cannot follow yourself")
       return data