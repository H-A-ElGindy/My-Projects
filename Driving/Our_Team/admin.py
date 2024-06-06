from django.contrib import admin
from . models import Team

@admin.register(Team)
class Admin(admin.ModelAdmin):
    list_display=['name','title']
    
