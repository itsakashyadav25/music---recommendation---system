
from django.db import models

class Profile(models.Model):
    user = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    movie = models.CharField(max_length=100)
    image = models.ImageField(upload_to='songs/images/')
    audio = models.FileField(upload_to='songs/audio/')
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name