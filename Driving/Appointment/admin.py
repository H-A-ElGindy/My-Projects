from django.contrib import admin
from .models import Appointment,Car_type

@admin.register(Appointment)
class Appointment_Admin(admin.ModelAdmin):
    list_display=['name','email','courses','car_type']

@admin.register(Car_type)
class Car_typeAdmin(admin.ModelAdmin):
    list_display=['car_type']
    

    



