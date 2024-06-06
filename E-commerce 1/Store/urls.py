
from django.urls import path
from .import views

app_name='Store'

urlpatterns = [
    path('',views.shop,name='shop'),
    path('Offer/',views.offer,name='offers'),
    path('search/',views.search,name='search'),
    path('<str:category_slug>/', views.shop,name='shop'),
    path('<str:category_slug>/<str:product_slug>/', views.detail,name='detail'),
   
    
    ]

