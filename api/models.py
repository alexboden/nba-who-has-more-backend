from django.db import models

class Game(models.Model):
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)