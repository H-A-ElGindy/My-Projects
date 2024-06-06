from django.urls import path
from . import views

app_name='Courses'
urlpatterns = [
    path('',views.courses,name='courses'),
    path('<str:course_slug>/',views.course_detail,name='course_detail'),
   
]