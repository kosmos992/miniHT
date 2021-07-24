from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser

class Movie(models.Model):
    title_kor = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)
    poster_url = models.TextField()
    rating_aud = models.CharField(max_length=50)
    rating_cri = models.CharField(max_length=50) 
    rating_net = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    showtimes = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    rate = models.CharField(max_length=50)
    summary = models.TextField()
class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image_url = models.TextField()
    movie = models.ForeignKey(Movie, null=True, on_delete=CASCADE, related_name='staff')

class CustomUser(AbstractUser):
  nickname = models.CharField(max_length=100)

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=CASCADE)
    movie = models.ForeignKey(Movie, null=True, on_delete=CASCADE)
    body = models.TextField()