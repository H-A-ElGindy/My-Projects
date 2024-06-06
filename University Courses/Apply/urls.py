from django.urls import path
from . import views

app_name='Apply'
urlpatterns = [
    path('Register/',views.register,name='register'),
    path('Login/',views.Login,name='login'),
    path('Logout/',views.Logout,name='logout'),
    path('Reset_Password/',views.reset_password,name='reset_password'),
    path('Profile/',views.profile,name='profile'),
    path('Edit_Profile/',views.edit_profile,name='edit_profile'),
    path('Application/',views.application,name='application')
]
