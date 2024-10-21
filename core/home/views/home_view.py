from django.shortcuts import render, redirect, get_object_or_404
from authz.models import GoogleClass
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')  
        cuser = User.objects.get(id = request.user.id)
        print(name,code)
        GoogleClass.objects.create(class_name=name, class_code=code, instructor = cuser)

    return render(request, 'index.html')