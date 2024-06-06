from django.http import HttpResponse
from django.shortcuts import render
from Categories.models import Category
from Store.models import Product,Offer
from django.db.models import Count
from django.contrib.auth.decorators import login_required



def home(request):
    try:
        categories=Category.objects.all().annotate(product_count=Count('product'))
        products=Product.objects.all()
        for product in products:
            try:
                offer=Offer.objects.get(product=product,is_active=True)
                product.offerprice=offer.offer_price()
                product.offerpercent=offer.percent
            except:
                pass     
    except:
        return HttpResponse('Product Does Not Exist')
   
    context={'categories':categories,'products':products}
    return render(request,'home/home.html',context)