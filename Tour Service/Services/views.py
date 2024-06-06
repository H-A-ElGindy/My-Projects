from django.shortcuts import render
from . models import Country,Travel_Guide,Category,Continent,Tour,Offer


def tours(request,slug=None):
    
    tours=Tour.objects.all()
    for tour in tours:
        try:
            offer=Offer.objects.get(tour=tour)
            tour.offer_price=offer.offer_price()
            tour.offer_percent=offer.percent
            tour.save()
        except:
            pass
    if slug!=None:
        category=Category.objects.get(slug=slug)
        tours=Tour.objects.filter(category=category)
        for tour in tours:
            try:
                offer=Offer.objects.get(tour=tour)
                tour.offer_price=offer.offer_price()
                tour.offer_percent=offer.percent
                tour.save()
            except:
                pass
    return render(request,'Tours/tour.html',{'tours':tours,'offer':offer})

def tour_detail(request,tour_slug,cat_slug=None):
    category=Category.objects.get(slug=cat_slug) 
    tour=Tour.objects.get(category=category,slug=tour_slug)
    return render (request,'Tours/tour_detail.html',{'tour':tour})

def offers(request):
    offers=Offer.objects.all()
    return render(request,'Tours/offers.html',{'offers':offers})


    