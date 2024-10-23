from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout


def handle_login(request):
    if request.method != 'POST':
        messages.info(request, 'Bad request')
        # return redirect('home')

    data = request.POST
    username = data.get('username')
    password = data.get('password')

    
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Log in the authenticated user
        login(request, user)
        messages.success(request, f'Welcome, {user.username}')
        return redirect('home')
    else:
        # If authentication fails, show an error message
        messages.error(request, 'Invalid username or password')
    return render(request, 'signin.html')
    

def user_logout(request):  
    logout(request) 
    messages.success(request,'Logout Sucessfully')
    return redirect('/auth/login')