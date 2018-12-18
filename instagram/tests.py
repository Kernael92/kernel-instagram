from django.test import TestCase
from .models import Image,Profile,Comment,Like
import datetime as dt 

# Create your tests here.

# class ProfileTestClass(TestCase):

#     #set up method
#     def setUp(self):
#         self.user = Profile(user = "Kerry", followers = 1, following = 2,profile_pic = 'photo', bio = "I am a go getter,ambitious and a very adventurous lady")
    
#     # Testing instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.user,Profile))
#      # Testing save method
#     def test_save_method(self):
#         self.user.save_profile()
#         profiles = Profile.objects.all()
#         self.assertTrue(len(profiles) > 0)
# class CommentTestClass(TestCase):
#     def setUp(self):
#         self.comment = Comment(post = 1, user = "Kerry", comment = "Awesome")
#     def test_instance(self):
#         self.assertTrue(isinstance(self.comment, Comment))
# class LikeTestClass(TestCase):
#     def setUp(self):
#         self.post = Like(post = 1, user = "Kerry")
#     def test_instance(self):
#         self.assertTrue(isinstance(self.post,Like))




# class ImageTestClass(TestCase):
#     # Set up method
#     # creating a new profile
#     def setUp(self):
#         self.user = Profile(user = "Kerry", followers = 1, following = 2,profile_pic = 'photo', bio = "I am a go getter,ambitious and a very adventurous lady")
    
#         self.user.save_profile()

#         self.new_image = Image(image = "image_url", image_name = 'beautiful', image_caption = "a beautiful image of the gorgeous model", profile = self.Kerry,)
#         self.new_image.save()

#     def tearDown(self):
#         Profile.objects.all().delete()
#         Image.objects.all().delete()
    
#     def test_get_instagram_date(self):
#         test_date = '2017-08-09'
#         date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
#         instagram_by_date = Image.days_instagram(date)
#         self.assertTrue(len(instagram_by_date) == 0)
     

        


