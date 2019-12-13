from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=50)
    platform = models.CharField(max_length= 50)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    publisher = models.CharField(max_length=50)
    n_players = models.IntegerField()

    # box_art = 
