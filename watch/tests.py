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
        
    def test_delete_profile(self):
        profile = Profile.objects.all().delete()
        self.assertTrue(len(profile)>0)
        
    def tearDown(self):
        Profile.objects.all().delete()
        
class TestNeigbourhood(TestCase):
    def setUp(self):
        
        self.hood = Neigbourhood(name = 'Kianda', description = 'Awesome hood', police_number = 0, health_number = 0 )
        self.hood.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neigbourhood))
        
    def test_save_hood(self):
        hood = Neigbourhood.objects.all()
        self.assertTrue(len(hood)>0)
        
    def test_delete_hood(self):
        hoods = Neigbourhood.objects.all().delete()
        self.assertTrue(len(hoods)>0)
        
        
class TestBusiness(TestCase):
    def setUp(self):
        self.user = User(username = 'Brian',email= 'g@gmail.com', password = '123')
        self.user.save()
        
        self.hood = Neigbourhood(name = 'Kianda', description = 'Awesome hood', police_number = 0, health_number = 0 )
        self.hood.save()
        
    
        self.biz = Business(name = 'kibandaski', email= 'k@gmail.com', description = 'startup restaturant', hood=self.hood, user=self.user)
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.biz, Business))
        
    def test_save_hood(self):
        business = Business.objects.all()
        self.assertTrue(len(business)>0)
        
    def test_delete_hood(self):
        business = Business.objects.all().delete()
        self.assertTrue(len(business)>0)
        
        
    
        
        
        
    
   