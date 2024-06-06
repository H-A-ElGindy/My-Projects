from django.shortcuts import render
from . models import Course

def courses(request):
    courses=Course.objects.all().filter(is_available=True)
    context={'courses':courses}
    return render (request,'Courses/courses.html',context)

def course_detail(request,course_slug):
    course=Course.objects.get(slug=course_slug,is_available=True)
    context={'course':course}
    return render (request,'Courses/Course_detail.html',context)