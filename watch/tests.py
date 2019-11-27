from django.test import TestCase
from . models import Post, Profile, Business, Neigbourhood
from django.contrib.auth.models import User

class  TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create( username = 'Brian',email= 'g@gmail.com', password = '123')
        self.user.save()
        
        self.hood = Neigbourhood.objects.create(id =1 ,name = 'Kianda', description = 'Awesome hood', police_number = 0, health_number = 0 )
        self.hood.save()
        
        self.profile = Profile.objects.create(name = 'Brian', bio='this is a test bio',profile_picture = 'test.jpeg', location = 'kibra',user=self.user, hood = self.hood)
        self.profile.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
        
    def save_profile(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
        
        
    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)
        
    def tearDown(self):
        Profile.objects.all().delete()
        
        
