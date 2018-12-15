from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Profile,Comment,Profile,Likes
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.auth.models import User
from . forms import PostPictureForm, ProfileEditForm, CommentForm
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    images = image.objects.all()
    return render(request, 'all-instagram/index.html', {"images":images})
