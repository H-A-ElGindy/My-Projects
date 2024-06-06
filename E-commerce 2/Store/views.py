from django.http import HttpResponse
from django.shortcuts import render
from .models import Category,Sub_Category,Product,Offer
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def subcategory(request,category_slug=None):
    try:
        category=Category.objects.get(category_slug=category_slug)
        sub_categories=Sub_Category.objects.filter(category=category)
    except:
        return HttpResponse('sub_category not found')
    context={'sub_categories':sub_categories}
    return render(request,'Store/Sub_Category.html',context)

def products(request,category_slug=None,sub_slug=None):
    products=Product.objects.all()
    if category_slug!=None and sub_slug!=None:
        try:
            category=Category.objects.get(category_slug=category_slug)
            sub_category=Sub_Category.objects.get(category=category,sub_slug=sub_slug)
            products=Product.objects.filter(sub_category=sub_category)   
            for product in products:
                try:
                    offer=Offer.objects.get(product=product)
                    product.pro_offer_price=offer.offer_price()
                    product.pro_offer_percent=offer.offer_percent
                    product.save()
                except:
                    pass
        except:
            return HttpResponse('products not found ')
    paginator = Paginator(products, 2)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'products':page_obj,'subcategory':sub_category}
    return render(request,'Store/Products.html',context)

def product_detail(request,category_slug=None,sub_slug=None,pro_slug=None):
    try:
        category=Category.objects.get(category_slug=category_slug)
        sub_category=Sub_Category.objects.get(category=category,sub_slug=sub_slug)
        product=Product.objects.get(sub_category=sub_category,pro_slug=pro_slug)
        try:
            offer=Offer.objects.get(product=product)
            product.pro_offer_price=offer.offer_price()
            product.pro_offer_percent=offer.offer_percent
            product.save()
        except:
                pass
    except:
        return HttpResponse('product not found')
    
    context={'product':product}
    return render(request,'Store/Product_detail.html',context)

def offers(request):
    offers=Offer.objects.all()
    paginator = Paginator(offers, 2)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'offers':page_obj}
    return render(request,'Store/Offers.html',context)


def search(request):
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        products=Product.objects.order_by('-created_at').filter(Q(pro_description__icontains=keywords) or Q(pro_name=keywords))
        return render(request,'Store/Search.html',{'products':products})
            

