from django.shortcuts import redirect, render
from . models import Appointment,Car_type
from Courses.models import Course

def reserve(request,course_slug):
    car_choices=Car_type.objects.all()
    courses=Course.objects.get(slug=course_slug)
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        car_type=request.POST['car_type']
        message=request.POST['message']

        name_exist=Appointment.objects.filter(name=name,courses=courses).exists()
        email_exist=Appointment.objects.filter(email=email,courses=courses).exists()
        
        if name_exist==True or email_exist==True:
            return render(request,'Error/already_exists.html')
        else:
            Appointment.objects.create(name=name,email=email,courses=courses,price=courses.price,car_type=car_type, Message=message)
            return render(request,'Error/Success.html')             
    else:
        context={'courses':courses,'car_choices':car_choices}
        return render(request,'Appointment/appointment.html',context)
            
