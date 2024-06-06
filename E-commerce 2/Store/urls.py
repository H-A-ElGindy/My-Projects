from django.urls import path
from . import views


app_name='Store'
urlpatterns = [
    path('search/',views.search,name='search'),
    path('offers/',views.offers,name='offers'),
    path('<str:category_slug>/',views.subcategory,name='sub_category'),
    path('<str:category_slug>/<str:sub_slug>/',views.products,name='products'),
    path('<str:category_slug>/<str:sub_slug>/<str:pro_slug>/',views.product_detail,name='product_detail'),
    
    
    ]