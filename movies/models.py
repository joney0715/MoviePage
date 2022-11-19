from django.db import models

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    runtime = models.IntegerField()
    tagline = models.TextField()
