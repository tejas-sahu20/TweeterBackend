from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tweet, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # Display username instead of user id
    tweet = serializers.PrimaryKeyRelatedField(read_only=True)  # Display tweet id instead of tweet details

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'author', 'tweet']


class TweetSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # Display username instead of user id
    comments = CommentSerializer(many=True, read_only=True)  # Include full comment details

    class Meta:
        model = Tweet
        fields = ['id', 'title', 'text', 'created_at', 'author', 'comments']


class UserSerializer(serializers.ModelSerializer):
    tweets = TweetSerializer(many=True, read_only=True)  # Include user's tweets

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'tweets']
        extra_kwargs = {
            "password": {"write_only": True},
            # "username": {"unique": True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
