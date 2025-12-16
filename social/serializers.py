from rest_framework.serializers import Serializer
from django.forms import fields
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    author = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = Post
        fields = ['author','content','id','image','created_at','updated_at']

    def validate(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("Post too long")
        return value