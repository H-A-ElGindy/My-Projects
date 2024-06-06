from django.db import models



class Car_type(models.Model):
    car_type=models.CharField(max_length=150)
    class Meta:
        verbose_name = ("car_type")
        verbose_name_plural = ("car_types")

    def __str__(self):
        return self.car_type


class Appointment(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    courses=models.CharField(max_length=150)
    car_type=models.CharField(max_length=150)
    Message=models.TextField()
    price=models.IntegerField()
    is_available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now=True,)

    class Meta:
        verbose_name = ("Appointment")
        verbose_name_plural = ("Appointments")

    def __str__(self):
        return self.name

    
