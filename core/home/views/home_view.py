from django.shortcuts import render, redirect, get_object_or_404
from authz.models import GoogleClass,Student
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def create_class(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')  
        cuser = User.objects.get(id = request.user.id)
        GoogleClass.objects.create(class_name=name, class_code=code, instructor = cuser)
    return render(request, 'index.html')


@login_required
def join_class(request):
    if request.method  == 'POST':
        jclassname = request.POST.get('name')
        jclasscode = request.POST.get('code')
        profilepic = request.Files.get('profilepic')
        googlecls = GoogleClass.objects.filter(name= jclassname).first()
        if googlecls is not None:
            if googlecls.code == jclasscode:
                cuser = request.user
                Student.objects.create(name = cuser,profilepic=profilepic,Student=googlecls)
                messages.success(request, 'You have successfully joined the class')
                return redirect('googleclass')
            else:
                messages.error(request, 'Invalid class code')

        else:
            messages.error(request,'this class does not exist')

    return render(request,'joinclass.html')  

        
        
        
