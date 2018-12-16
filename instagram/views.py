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
def following(request, username):
    user = User.objects.get(username=username)
    user_profile =Profile.objects.get(user=user)
    profiles = user_profile.following.all

    context = {
        'header': 'Following',
        'profiles': profiles
    }
    return render(request, 'all-instagram/follow_list.html', context)

def post_picture(request):
    if request.method == 'POST':
        form = PostPictureForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = Image(user_profile=request.user.profile,
                          image_name=request.POST['image_name'],
                          image=request.FILES['image'],
                          image_caption=request.POST['image_caption'],
                          posted_on=datetime.datetime.now())
            post.save()
            return redirect(reverse('profile', kwargs={'username': request.user.username}))
    else:
        form = PostPictureForm()

    context = {
        'form': form
    }
    return render(request, 'all-instagram/post_picture.html', context)

def post(request, pk):
    post = Image.objects.get(pk=pk)
    try:
        like = Like.objects.get(post=post, user=request.user)
        like = 1
    except:
        like = None
        like = 0

    context = {
        'post': post,
        'like': like
    }
    return render(request, 'all-instagram/post.html', context)

def likes(request, pk):
    

    post = Image.objects.get(pk=pk)
    profiles = Like.objects.filter(post=post)

    context = {
        'header': 'Likes',
        'profiles': profiles
    }
    return render(request, 'all-instagram/follow_list.html', context)

def add_like(request):
    post_pk = request.POST.get('post_pk')
    post =Image.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }

def add_comment(request):
    comment_text = request.POST.get('comment_text')
    post_pk = request.POST.get('post_pk')
    post = IGPost.objects.get(pk=post_pk)
    commenter_info = {}

    try:
        comment = Comment(comment=comment_text, user=request.user, post=post)
        comment.save()

        username = request.user.username
        profile_url = reverse('profile', kwargs={'username': request.user})

        commenter_info = {
            'username': username,
            'profile_url': profile_url,
            'comment_text': comment_text
        }


        result = 1
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'post_pk': post_pk,
        'commenter_info': commenter_info
    }

def follow_toggle(request):
    user_profile =Profile.objects.get(user=request.user)
    follow_profile_pk = request.POST.get('follow_profile_pk')
    follow_profile = Profile.objects.get(pk=follow_profile_pk)

    try:
        if user_profile != follow_profile:
            if request.POST.get('type') == 'follow':
                user_profile.following.add(follow_profile)
                follow_profile.followers.add(user_profile)
            elif request.POST.get('type') == 'unfollow':
                user_profile.following.remove(follow_profile)
                follow_profile.followers.remove(user_profile)
            user_profile.save()
            result = 1
        else:
            result = 0
    except:
        result = 0

    return {
        'result': result,
        'type': request.POST.get('type'),
        'follow_profile_pk': follow_profile_pk
    }

