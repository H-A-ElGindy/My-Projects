from django.contrib import admin
from . models import Booking

@admin.register(Booking)
class Booking_Admin(admin.ModelAdmin):
    list_display=['user','tour','date','booking_price']
    
