from django.db import models


class Genre(models.Model):
    """ Genre of the movie (Action, Thriller, etc.) """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """ The movie model """
    name = models.CharField(max_length=250)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    stars = models.FloatField(default=1.0)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """ Comment from users about the movie """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    comment = models.TextField()
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
