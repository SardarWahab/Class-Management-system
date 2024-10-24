from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout


def handle_login(request):
    data = request.POST
    username = data.get('username')
    password = data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, f'Welcome, {user.username}')
        return redirect('home')
    else:
        messages.error(request, 'Invalid username or password')
    return render(request, 'signin.html')
    

def user_logout(request):  
    logout(request) 
    messages.success(request,'Logout Sucessfully')
    return redirect('/auth/login')