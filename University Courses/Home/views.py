from django.shortcuts import render
from . models import Succes_Student,Existing_Student,New_Student,Current_Teacher,Award

def home(request):
    exist=Existing_Student.objects.count()
    success=Succes_Student.objects.count()
    new_students=New_Student.objects.count()
    current_teachers=Current_Teacher.objects.count()
    award=Award.objects.count()
    success_rate=(success/exist)*100
    context={'new':new_students,'current':current_teachers,'award':award,'success':success_rate}
    return render(request,'Home/Home.html',context)
