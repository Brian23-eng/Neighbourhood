from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt



class Neigbourhood(models.Model):
    name = models.CharField(max_length=120, blank=False)
    description = models.TextField(max_length=500, blank=False)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='ad')
    location = models.CharField(max_length=60)
    hood_logo = models.ImageField(upload_to='images/')
    police_number = models.IntegerField(null=True, blank=True)
    health_number = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.name}Neigbourhood'
    
    def create_hood(self):
        self.save()
        
    def save_hood(self):
        self.save()
        
    def delete_hood(self):
        self.delete()
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=120, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=120, blank=False)
    hood = models.ForeignKey(Neigbourhood, on_delete=models.SET_NULL, related_name='member', blank=True, null=True )
    
    def __str__(self):
        return f'{self.username}Profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    def delete_profile(self):
        self.delete()
        
    def save_profile(self):
        self.save()
    
    
    



class Business(models.Model):
    name = models.CharField(max_length=120, blank=False)
    email = models.EmailField()
    description = models.TextField(max_length=500, blank=True)
    hood = models.ForeignKey(Neigbourhood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    
    def __str__(self):
        return f'{self.name}Neigbourhood'
    
    


class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Neigbourhood, on_delete=models.CASCADE, related_name='hood_post')