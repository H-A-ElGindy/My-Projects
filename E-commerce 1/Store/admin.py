from django.contrib import admin
from Store.models import Product,Offer

# Register your models here.
@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    list_display=['name','slug','category','price','created_at']

@admin.register(Offer)
class Offer_Admin(admin.ModelAdmin):
    list_display=['product','percent','created_at']


    

    


    
