from django.contrib import admin
from .models import Existing_Student,Succes_Student,New_Student,Current_Teacher,Award

@admin.register(Existing_Student)
class Existing_Admin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Succes_Student)
class Succes_Admin(admin.ModelAdmin):
    list_display=['name']  

@admin.register(New_Student)
class New_Admin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Current_Teacher)
class Current_Admin(admin.ModelAdmin):
    list_display=['name'] 


@admin.register(Award)
class Award_Admin(admin.ModelAdmin):
    list_display=['name']         



