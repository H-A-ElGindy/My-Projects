from django.db import models
from Services.models import Tour
from django.contrib.auth.models import User


class Booking(models.Model):
    tour=models.ForeignKey(Tour, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.CharField(max_length=50)
    booking_price=models.IntegerField()
    special=models.TextField()

    class Meta:
        verbose_name = ("Booking")
        verbose_name_plural = ("Bookings")

    def __str__(self):
        return str(self.tour)

    
