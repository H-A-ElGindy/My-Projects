from django.contrib import admin
from . models import Category,Sub_Category,Product,Offer

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display=['category_name','category_slug','created_at']
    
@admin.register(Sub_Category)
class Sub_Category_Admin(admin.ModelAdmin):
    list_display=['category','sub_name','sub_slug','created_at']

@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    list_display=['sub_category','pro_name','pro_slug','pro_stock','pro_price','pro_offer_price','pro_offer_percent','created_at']

@admin.register(Offer)
class Offer_Admin(admin.ModelAdmin):
    list_display=['product','offer_percent','is_active']