from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField('Profile',related_name="profile_followers",blank=True)
    following = models.ManyToManyField('Profile',related_name="following_profile", blank=True)
    profile_pic = ProcessedImageField(upload_to='profile_pics',format="JPEG",options={'quality':100},null=True,blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)

    def get_number_of_followers(self):
        print(self.followers.count())
        if self.followers.count():
            return self.followers.count()
        else:
            return 0
    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0 
    def __str__(self):
        return self.user.username

class Image(models.Model):
    user_profile = models.ForeignKey(Profile,null=True, blank=True)
    image_name = models.CharField(max_length=100)
    image = ProcessedImageField(upload_to='images/',format='JPEG',options={'quality':100})
    image_caption = models.CharField(max_length =254)
    posted_on = models.DateTimeField(default=datetime.now)

    def get_number_of_likes(self):
        return self.like_set.count()
    def get_number_of_comments(self):
        return self.comment_set.count()

    def __str__(self):
        return self.image_name

class Comment(models.Model):
    post = models.ForeignKey(Image)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comment
class Like(models.Model):
    post = models.ForeignKey(Image)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like ' + self.user.username + '' + self.post.image_name
    
    
