from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from core.models import Profile

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

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
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
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