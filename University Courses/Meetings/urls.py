from django.urls import path
from . import views


app_name='Meetings'
urlpatterns = [
    path('',views.meeting,name='meetings'),
    path('<str:slug>/',views.meeting_detail,name='meeting_detail'),
]

