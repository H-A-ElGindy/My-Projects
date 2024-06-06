from django.http import HttpResponse
from django.shortcuts import render
from . models import Booking,Tour
from Services.models import Offer
from django.contrib.auth.decorators import login_required
from . forms import Booking_Form


@login_required(login_url='Accounts:login')
def booking(request):
    book=Booking()
    book.user=request.user
    if request.method=="POST":
        tour=request.POST['tour']
        date=request.POST['date']
        special=request.POST['special']
        form=Booking_Form(request.POST,instance=book)
        if form.is_valid():
            booking_exist=Booking.objects.filter(user=request.user,tour=tour,date=date).exists()
            if booking_exist==True:
                return HttpResponse('Booking Submitted Before') 
            book.special=special
            if book.tour.offer_price:
                book.booking_price=book.tour.offer_price
            else:
                book.booking_price=book.tour.price
            form.save()
            book.save()
            return HttpResponse('Booking Submitted')
        
    form=Booking_Form(instance=book)
    return render(request,'Booking/booking.html',{'form':form})