from django.urls import path
from . import views

app_name='Appointment'
urlpatterns = [path('<str:course_slug>/',views.reserve,name='user_appointment'),]