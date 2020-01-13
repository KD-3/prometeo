from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    carousel = Carousel.objects.all()
    return render(request, 'home.html', {'carousel' : carousel})

def home_redirect(request):
    return redirect(home)

def team(request):
    members = Coordinator.objects.all()
    _roles = {
        'pr_team_member': 'PR Team Members',
        'coordinator': 'Coordinator',
        'workshop_coordinator': 'Workshop Coordinators',
        'technical_coordinator': 'Technical Event Coordinators',
        'informal_coordinator': 'Informal Event Coordinators',
        'webd_team_member': 'WebD Team Members', 
    }
    roles = {}
    for role, display in _roles.items():
        if(Coordinator.objects.filter(role=role).exists()):
            roles[role] = display
    return render(request, 'our_team.html', {'members':members, 'roles' : roles})

def industry_day(request):
    return render(request, 'industry_day.html')