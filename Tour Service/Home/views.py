from django.shortcuts import render
from Services.models import Category,Travel_Guide

def Home(request):
    categories=Category.objects.all()
    return render(request,'Home/Home.html',{'categories':categories})
def about(request):
    return render(request,'Home/about.html')