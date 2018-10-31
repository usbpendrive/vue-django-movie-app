from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Genre, Movie, Comment
from .serializers import UserSerializer, GenreSerializer, MovieSerializer, CommentSerializer


class UserList(generics.ListAPIView):
    """ View to list all users """
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class UserCreate(generics.CreateAPIView):
    """ View to create a new user. Only accepts POST requests """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a user to update user information
    Accepts GET and PUT requests and the record id must be provided in the request
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class GenreListCreate(generics.ListCreateAPIView):
    """ List and create genre """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticated, )


class GenreRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve and update genre information """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MovieListCreate(generics.ListCreateAPIView):
    """ List and create movie """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MovieRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve and update movie information """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CommentListCreate(generics.ListCreateAPIView):
    """ List and create comment """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CommentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve and update comment information """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, )
