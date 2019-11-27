from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt



class Neigbourhood(models.Model):
    name = models.CharField(max_length=120, blank=False)
    dscription = models.TextField(max_length=500, blank=False)
    police_number = models.IntegerField(null=True, blank=True)
    health_number = models.IntegerField(null=True, blank=True)
    
    
    
class Profile(models.Model):
    pass



class Business(models.Model):
    pass


class Post(models.Model):
    pass