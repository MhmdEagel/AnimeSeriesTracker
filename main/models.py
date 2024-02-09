from django.db import models

# Create your models here.
class Anime(models.Model):
    name = models.CharField(max_length=255)
    episodes = models.IntegerField()
    synopsis = models.TextField()
    rating = models.FloatField()
    studio = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()