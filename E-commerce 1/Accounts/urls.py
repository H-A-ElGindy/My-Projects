from django.urls import path
from .import views

app_name='Accounts'

urlpatterns = [
   
    path('profile/',views.profile,name='profile'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('register/',views.register,name='register'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('reset_password/',views.reset_password,name='reset_password'),
   
 ]
    