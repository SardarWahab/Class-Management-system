from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from ..models import User
# from django.contrib.auth.models import User

def handle_reg(request):
    if request.method != 'POST':
        messages.info(request,'Please sumbmit a form to Register')
        return redirect('home')
    
    data = request.POST
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    password2 = data.get('password2')


    if password != password2:
        messages.info(request,'Passwords do not match')
        return redirect('home')
    if User.objects.filter(username=username).exists():
        messages.warning(request,"username already exists")
        return redirect('home')
    if User.objects.filter(email=email).exists():
        messages.warning(request,"Email already exists")
        return redirect('home')
    
    new_user = User.objects.create(username=username,email=email)
    new_user.set_password(password)
    new_user.save()
    messages.success(request,'Registration successfully')
    return redirect('home') 

