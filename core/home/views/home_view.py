from django.shortcuts import render, redirect
from authz.models import GoogleClass,Student
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def home(request):
    current_user = request.user
    googlcls = GoogleClass.objects.filter(instructor__username = current_user)
    std = Student.objects.filter(name=current_user)
    context = {
        'classs': googlcls,
        'std': std
    }
    return render(request,'home.html',context)

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
    if request.method == 'POST':
        jclassname = request.POST.get('name')
        jclasscode = request.POST.get('code')
        profilepic = request.FILES.get('profilepic')  # Note: 'FILES' should be in uppercase
        googlecls = GoogleClass.objects.filter(class_name=jclassname).first()
        
        if googlecls is not None:
            if googlecls.class_code == jclasscode:
                cuser = request.user
                # Create the student object using the correct field
                Student.objects.create(name=cuser, profilepic=profilepic)  # Assuming profilepic is a field in the Student model
                messages.success(request, 'You have successfully joined the class')
                return redirect('home')  # Replace 'home' with the correct redirect URL
            else:
                messages.error(request, 'Invalid class code')
        else:
            messages.error(request, 'This class does not exist')

    return render(request, 'joinclass.html')

        
        
        
