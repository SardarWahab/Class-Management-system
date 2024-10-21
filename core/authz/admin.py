from django.contrib import admin
from authz.models import *
# Register your models here.
admin.site.register((User,SubmittedAssignment,Assignment,Resources,Classroom))
