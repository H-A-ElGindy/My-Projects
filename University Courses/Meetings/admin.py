from django.contrib import admin
from . models import Meeting

@admin.register(Meeting)
class Meeting_Admin(admin.ModelAdmin):
    list_display=['title','date','price','Hours_1','Hours_2','location_1','location_2','book_1','book_2']
    

