from django.urls import path
from . import views

app_name='Accounts'
urlpatterns = [
    
    path('Register/',views.register,name='register'),
    path('Login/',views.Login,name='login'),
    path('Logout/',views.log_out,name='logout'),
    path('Reset/',views.reset_password,name='reset_password'),
    path('Profile/',views.profile,name='profile'),
    path('Edit_Profile/',views.edit_profile,name='edit_profile'),
 
]