from django.urls import path
from .views import login_view  # or other view functions/classes you need
from .views import Registration_view


# from .views import login_view, Registeration_view 
urlpatterns = [
    path('login/',login_view.handle_login, name='login'),
    path('logout/', login_view.user_logout, name='logout'),
    path('register/',Registration_view.handle_reg, name='register'),
]