from django.urls import path
from . import views

app_name='Services'
urlpatterns = [
    
    
    path('',views.tours,name='tours'),
    path('offers/',views.offers,name='offers'),
    path('<str:slug>/',views.tours,name='tours'),
    path('<str:cat_slug>/<str:tour_slug>/',views.tour_detail,name='tour_detail'),
   
    
   
    
]