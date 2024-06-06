from django.contrib import admin
from . models import Cart_item,Variation,Coupon,Order,OrderProduct
# Register your models here.

@admin.register(Cart_item)
class Cart_item_Admin(admin.ModelAdmin):
    list_display=['product','quantity','is_active']

@admin.register(Variation)
class Variation_Admin(admin.ModelAdmin):
    list_display=['product','color_value','size_value']
    
@admin.register(Coupon)
class Coupon_Admin(admin.ModelAdmin):
    list_display=['name','percent']

@admin.register(Order)
class Order_Admin(admin.ModelAdmin):
    list_display=['user','f_name','l_name','email','phone','city','total_checkout','is_active']

@admin.register(OrderProduct)
class OrderProduct_Admin(admin.ModelAdmin):
    list_display=['user','order','product','product_price','quantity','is_ordered']
