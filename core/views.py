from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from core.models import Profile
from core.models import Post
from core.models import LikePost

# Create your views here.

@login_required(login_url='login')
def index(request):
    user_object = User.objects.get(username = request.user.username)
    user_profile = Profile.objects.get(user = user_object)
    
    posts = Post.objects.all()

    return render(request, 'index.html', {'user_profile': user_profile, 'posts': posts})

def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm-password']
        
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, first_name = "", second_name = "")
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
        
    else:
        return render(request, 'login.html')
    
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        if request.FILES.get('image') is None:
            image = user_profile.profile_img
            bio = request.POST['bio']
            location = request.POST['location']
            first_name = request.POST['first_name']
            second_name = request.POST['second_name']
            
            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.first_name = first_name
            user_profile.second_name = second_name
            user_profile.save()
        
        if request.FILES.get('image') is not None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            first_name = request.POST['first_name']
            second_name = request.POST['second_name']
            
            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.first_name = first_name
            user_profile.second_name = second_name
            user_profile.save()
            
        return redirect('settings')
    
    return render(request, 'settings.html', {'user_profile': user_profile})

@login_required
def upload(request):
    
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        
        return redirect('/')
    else:
        return redirect('/')

@login_required
def profile(request, pk):
    
    user_object = User.objects.get(username = pk)
    user_profile = Profile.objects.get(user = user_object)
    posts = Post.objects.filter(user =pk)
    request_object = User.objects.get(username = request.user.username)
    request_profile = Profile.objects.get(user = request_object)
    
    
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': posts,
        'request_profile': request_profile,
    }
    
    return render(request, 'profile.html', context)


def like(request):
    username = request.user.username
    post_id = request.GET.get('post_id')
    
    post = Post.objects.get(id=post_id)
    
    filter = LikePost.objects.filter(post_id=post_id, username=username).first()
    
    if filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.likes = post.likes + 1
        post.save()
        return redirect('/')
    else:
        filter.delete()
        post.likes = post.likes - 1
        post.save()
        return redirect('/')
    