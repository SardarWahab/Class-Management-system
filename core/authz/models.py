from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    rollno = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    profile = models.ImageField(upload_to='profile_image', blank=True, null=True)
    classrooms = models.ForeignKey('Classroom', blank=True, related_name='students', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

class Classroom(models.Model):
    department = models.CharField(max_length=50)
    session = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.department} ({self.session})"

class Resources(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='resources', blank=True, null=True)
    content = models.FileField(upload_to='resources/', blank=True, null=True)
    extra_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Resource {self.id} for {self.classroom}"

class Assignment(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    content = models.FileField(upload_to='assignments/assign', blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.subject} for {self.classroom}"

class SubmittedAssignment(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='uploads')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_assignment')
    content = models.FileField(upload_to='assignments/submission', blank=False, null=False)
    submission_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Upload by {self.student.username} for {self.assignment.title}"
