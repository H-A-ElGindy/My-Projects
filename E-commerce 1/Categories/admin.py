from django.contrib import admin
from .models import Category

# Register your models here.
@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display=['name','slug','created_at']
    
