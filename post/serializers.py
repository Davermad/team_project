from rest_framework import serializers

from .models import Post, Rating, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['user', ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
