from django.shortcuts import render
from . models import Team


def team(request):
    teams=Team.objects.all()
    context={'teams':teams}
    return render(request,'Team/team.html',context)
    
