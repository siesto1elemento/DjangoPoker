from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Game(models.Model):
    GameID = models.IntegerField(primary_key=True)
    GameName = models.CharField(max_length=20,default="My Online Game")
    STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='waiting')
    Maxplayers = models.IntegerField(validators=[MaxValueValidator(10)])
    StartCash = models.IntegerField(default=3000)
    Smallblind = models.IntegerField(default=10)
    Raiseblind = models.IntegerField(default=8)
    Timeout = models.IntegerField(default=5)
    delay = models.IntegerField(default=5)

class Player(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)






