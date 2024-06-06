from django.contrib import admin
from . models import Category,Travel_Guide,Tour,Country,Continent,Offer

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display=['name','slug','is_available']

@admin.register(Continent)
class Country_Admin(admin.ModelAdmin):
    list_display=['name','slug']    

@admin.register(Travel_Guide)
class Travel_Guide_Admin(admin.ModelAdmin):
    list_display=['name','is_available']

@admin.register(Tour)
class Tour_Admin(admin.ModelAdmin):
    list_display=['continent','country','city','travel_guide','price','is_available']

@admin.register(Country)
class Country_Admin(admin.ModelAdmin):
    list_display=['continent','name','slug']

@admin.register(Offer)
class Offer_Admin(admin.ModelAdmin):
    list_display=['tour','percent']