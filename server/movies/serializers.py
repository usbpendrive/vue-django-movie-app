from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Genre, Movie, Comment


class UserSerializer(serializers.ModelSerializer):
    """ A serializer for User class """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'is_active', 'is_superuser')


class GenreSerializer(serializers.ModelSerializer):
    """ A serializer for Genre class """
    class Meta:
        model = Genre
        fields = ('id', 'name', 'description')


class MovieSerializer(serializers.ModelSerializer):
    """ A serializer for Movie class """
    class Meta:
        model = Movie
        fields = ('id', 'name', 'genre', 'stars', 'description', 'created')


class CommentSerializer(serializers.ModelSerializer):
    """ A serializer for Comment class """
    class Meta:
        model = Comment
        fields = ('id', 'user', 'movie', 'comment', 'visible', 'created')
