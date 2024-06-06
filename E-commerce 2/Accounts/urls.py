from django.urls import path
from . import views


app_name='Accounts'
urlpatterns = [
    path('Register/',views.sign_up,name='register'),
    path('Login/',views.log_in,name='login'),
    path('Logout/',views.log_out,name='logout'),
    path('reset_password/',views.reset_password,name='reset_password'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    ]