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
        'coordinator': 'Coordinator',
        'webd_team_member': 'WebD Team', 
        'pr_team_member': 'PM & PR Team',
        'technical_coordinator': 'Technical Event Team',
        'creativity_team_member': 'Branding Team', 
        'informal_coordinator': 'Informal Event Team',
        'workshop_coordinator': 'Workshop Team',
    }
    roles = {}
    for role, display in _roles.items():
        if(Coordinator.objects.filter(role=role).exists()):
            roles[role] = display
    return render(request, 'our_team.html', {'members':members, 'roles' : roles})

def industry_day(request):
    return render(request, 'industry_day.html')