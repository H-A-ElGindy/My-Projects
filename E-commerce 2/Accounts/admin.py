from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class Prfoile_Admin(admin.ModelAdmin):
    list_display=['user','phone','image']

    

