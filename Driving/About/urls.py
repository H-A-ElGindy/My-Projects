from django.urls import path
from . import views

app_name='About'
urlpatterns = [
    path('',views.about,name='about'),
   
]