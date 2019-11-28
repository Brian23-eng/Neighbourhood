from django.test import TestCase
from . models import Post, Profile, Business, Neigbourhood
from django.contrib.auth.models import User

class  TestProfile(TestCase):
    def setUp(self):
        self.user = User(username = 'Brian',email= 'g@gmail.com', password = '123')
        self.user.save()
        
        self.hood = Neigbourhood(name = 'Kianda', description = 'Awesome hood', police_number = 0, health_number = 0 )
        self.hood.save()
        
        self.profile = Profile(user=self.user, name='Brian', bio='this is a test bio',profile_picture = 'test.jpeg', location = 'kibra', hood = self.hood)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
        
    def test_save_profile(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
        
    
   