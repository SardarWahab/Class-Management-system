from .views import home_view
from django.urls import path
urlpatterns = [
    path('',home_view.home, name='home'),
     path('joinclass/', home_view.join_class, name='joinclass'),
     path('createclass/', home_view.create_class, name='createclass'),
     path('resource/<int:id>/',home_view.resources,name='resource')
]