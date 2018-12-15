from django import forms
from django.forms import ModelForm
from imagekit.forms import ProcessedImageField
from .models import Image, Profile, Comment 

class PostPictureForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image_name', 'image']
# class ProfileEditForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['profile_pic','bio']
# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['comment']