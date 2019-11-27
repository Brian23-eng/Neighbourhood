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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=120, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=120, blank=False)
    hood = models.ForeignKey(Neigbourhood, on_delete=models.SET_NULL, related_name='member', blank=True, null=True )
    



class Business(models.Model):
    name = models.CharField(max_length=120, blank=False)
    email = models.EmailField()
    description = models.TextField(max_length=500, blank=True)
    hood = models.ForeignKey(Neigbourhood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    


class Post(models.Model):
    pass