from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Profile,Comment,Profile,Like
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.auth.models import User
from . forms import PostPictureForm, ProfileEditForm, CommentForm
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    images = Image.objects.all()
    return render(request, 'all-instagram/index.html', {"images":images})
def profile(request, username):
    user = User.objects.get(username=username)
    if not user:
        return redirect('index')

    profile = Profile.objects.get(user=user)
    context = {
        'username': username,
        'user': user,
        'profile': profile
    }
    return render(request, 'all-instagram/profile.html', context)

def profile_settings(request, username):
    user = User.objects.get(username=username)
    if request.user != user:
        return redirect('index')

    if request.method == 'POST':
        print(request.POST)
        form = ProfileEditForm(request.POST, instance=user.profile, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile', kwargs={'username': user.username}))
    else:
        form = ProfileEditForm(instance=user.userprofile)

    context = {
        'user': user,
        'form': form
    }
    return render(request, 'all-instagram/profile_settings.html', context)
def followers(request, username):
    user = User.objects.get(username=username)
    user_profile =Profile.objects.get(user=user)
    profiles = user_profile.followers.all

    context = {
        'header': 'Followers',
        'profiles': profiles,
    }

    return render(request, 'all-instagram/follow_list.html', context)
