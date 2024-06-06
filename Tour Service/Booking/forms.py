from django import forms
from .models import Booking

class Booking_Form(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        exclude= 'user','booking_price',