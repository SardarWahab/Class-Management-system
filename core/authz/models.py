from django.db import models
from django.contrib.auth.models import User

# GoogleClass Model
class GoogleClass(models.Model):
    class_name = models.CharField(max_length=255)
    class_code = models.CharField(max_length=100)
    instructor = models.ForeignKey(User, null=True, blank=True ,on_delete=models.CASCADE)  

    def __str__(self):
        return self.class_name

class Student(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic = models.FileField(upload_to='image/',null=True,blank=True)
    students = models.ForeignKey(GoogleClass,on_delete=models.CASCADE,null=True,related_name='classinstructor')
    

    # def __str__(self):
    #     return self.name


# ClassData Model
class ClassData(models.Model):
    name = models.ForeignKey(GoogleClass, on_delete=models.CASCADE,related_name='googleclss')
    announcement = models.TextField()
    lectures = models.FileField(upload_to='resources/', blank=False,null=True)
 

    # def __str__(self):
    #     return self.name


# Assignment Model
class Assignment(models.Model):
    assignment_name = models.CharField(max_length=255)
    content = models.FileField(upload_to='files/',blank= True,null=True) 
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.assignment_name


# UploadAssignment Model
class UploadAssignment(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file_url = models.FileField(upload_to='files/',blank= True,null=True)  # File path or URL
    submitted_at = models.DateTimeField(auto_now_add=True)

    
