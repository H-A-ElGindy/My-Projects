from django.urls import path
from . import views


app_name='Courses'
urlpatterns = [
    path('',views.courses,name='courses'),
    path('<str:slug>',views.course_detail,name='course_detail'),
]
