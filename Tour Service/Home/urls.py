from django.urls import path
from . import views

app_name='Home'
urlpatterns = [
    
    path('',views.Home,name='home'),
    path('About/',views.about,name='about'),
]