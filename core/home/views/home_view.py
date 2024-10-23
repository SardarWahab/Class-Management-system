from django.shortcuts import render, redirect
from authz.models import GoogleClass,Student,ClassData
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def home(request):
   
    current_user = request.user
    googlcls = GoogleClass.objects.filter(instructor__username = current_user)
    # googlclss = GoogleClass.objects.filter(classinstructor__name__username = current_user)
    # if current_user.is_authenticated:
    googlclss = Student.objects.filter(name=current_user)
    # else:
    #    return redirect('home')      
    # print(googlclss)
    # std = Student.objects.filter(name=current_user)
    context = {
        'classs': googlcls,
        'std': googlclss,
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
        profilepic = request.FILES.get('profilepic')
        googlecls = GoogleClass.objects.filter(class_name=jclassname).first()
        
        if googlecls is not None:
            if googlecls.class_code == jclasscode:
                cuser = request.user
                
                Student.objects.create(name=cuser, profilepic=profilepic, students = googlecls)  
                messages.success(request, 'You have successfully joined the class')
                return redirect('home') 
            else:
                messages.error(request, 'Invalid class code')
        else:
            messages.error(request, 'This class does not exist')

    return render(request, 'joinclass.html')

def resources(request,id):
    googlcls = GoogleClass.objects.get(id=id)
    if request.method == 'POST':
        name=googlcls
        announcement = request.POST.get('announcement')
        lectures = request.FILES.get('lectures')
        ClassData.objects.create(announcement=announcement,lectures=lectures,name=name)
        messages.success(request, 'You have successfully uploaded the resources')
        
    get_resource = GoogleClass.objects.filter(id=id).first()
    get_re = get_resource.googleclss.all()
    print(get_re)
    context ={
        'get': get_resource,
        'get_re': get_re
    }
    
    return render(request,'resources.html',context)
        

        
