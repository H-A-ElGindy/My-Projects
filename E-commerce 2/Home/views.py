from django.shortcuts import render
from Store.models import Category,Sub_Category

# Create your views here.
def Home(request,):
    categories=Category.objects.all()
    for category in categories:
        subcategories=Sub_Category.objects.filter(category=category)
    context={'categories':categories,'subcategories':subcategories}
    return render(request,'Home/Home.html',context)
       
        