from django.contrib import admin
from . models import Profile,Application

@admin.register(Profile)
class Profile_Admin(admin.ModelAdmin):
    list_display=['user','phone']
    
@admin.register(Application)
class Application_Admin(admin.ModelAdmin):
    list_display=['user','course','phone','city','address','school']
