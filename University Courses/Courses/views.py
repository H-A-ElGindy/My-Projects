from django.shortcuts import render
from .models import Course
from django.core.paginator import Paginator

def courses(request):
    courses=Course.objects.all()
    paginator = Paginator(courses, 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'courses':page_obj}
    return render(request,'Courses/Courses.html',context)

def course_detail(request,slug):
    course=Course.objects.get(slug=slug)
    context={'course':course}
    return render(request,'Courses/Course_detail.html',context)