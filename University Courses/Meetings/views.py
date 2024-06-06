from django.shortcuts import render
from .models import Meeting
from django.core.paginator import Paginator




def meeting(request):
    meetings=Meeting.objects.all().order_by('date')
    paginator = Paginator(meetings, 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'meetings':page_obj}
    return render(request,'Meetings/Meetings.html',context)

def meeting_detail(request,slug):
    meeting=Meeting.objects.get(slug=slug)
    context={'meeting':meeting}
    return render(request,'Meetings/Meeting_detail.html',context)