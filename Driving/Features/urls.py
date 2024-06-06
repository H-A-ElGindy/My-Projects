from django.urls import path
from . import views

app_name='Features'
urlpatterns = [
    path('',views.feature,name='features'),
   
]