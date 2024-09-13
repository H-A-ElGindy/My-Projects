from django.contrib import admin
from . models import*


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','first_name','last_name','phone','designation','joined_at','image_tag','is_available']
    readonly_fields=['image_tag']
    
   
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['profile','title','created_at','updated_at','file_tag']
    readonly_fields=['file_tag']
    
