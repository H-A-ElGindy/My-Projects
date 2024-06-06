from django.shortcuts import render


def feature(request):
    return render(request,'Features/feature.html')