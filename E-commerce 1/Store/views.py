from itertools import product
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Offer
from Categories.models import Category
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def shop(request,category_slug=None):
   
    if category_slug!=None:
        category=Category.objects.get(slug=category_slug,is_available=True)
        products=Product.objects.all().filter(category=category,is_available=True)
        for product in products:
            try:
                offer=Offer.objects.get(product=product,is_active=True)
                product.offerprice=offer.offer_price()
                product.offerpercent=offer.percent
            except:
                pass
    else:
        products=Product.objects.all()
        for product in products:
            try:
                offer=Offer.objects.get(product=product,is_active=True)
                product.offerprice=offer.offer_price()
                product.offerpercent=offer.percent
            except:
                pass
            
    paginator = Paginator(products, 2)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={'products':page_obj,}
    return render(request,'store/store.html',context)

def detail(request,category_slug,product_slug,offers=None,final_price=0):
    
    try:
        category=Category.objects.get(slug=category_slug)
        product=Product.objects.get(slug=product_slug,category=category,is_available=True)
    except:
        return HttpResponse('Product Does Not Exist')
    try:
        offers=Offer.objects.get(product=product)
        final_price=offers.offer_price()
        product.offerpercent=offers.percent
    except:
        pass

    context={'product':product,'offers':offers,'final_price':final_price}
    return render(request,'store/product_detail.html',context)

def offer(request):
    offers=Offer.objects.all().filter(is_active=True)
    context={'offers':offers}
    return render(request,'store/offers.html',context)

def search(request):
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        products=Product.objects.order_by('-created_at').filter(Q(description__icontains=keywords) or Q(name=keywords))
        return render(request,'store/search.html',{'products':products})