from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User,

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField('Profile',related_name="profile_followers",blank=True)
    following = models.ManyToManyField('Profile',related_name="following_profile", blank=True)
    profile_pic = ProcessedImageField(upload_to='profile_pics',format="JPEG",options={'quality':100},null=True,blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)

