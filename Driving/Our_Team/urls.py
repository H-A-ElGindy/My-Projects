from django.urls import path
from . import views

app_name='Our_Team'
urlpatterns = [
    path('',views.team,name='team'),
   
]