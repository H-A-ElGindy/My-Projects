from django.contrib import admin
from .models import Course

@admin.register(Course)
class Admin(admin.ModelAdmin):
    list_display=['title','price','Hours','location']
    

