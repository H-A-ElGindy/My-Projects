from django.contrib import admin
from .models import Course
# Register your models here.

@admin.register(Course)
class Course_Admin(admin.ModelAdmin):
    list_display=['name','slug','level','Duration','duration_type','price']
    
