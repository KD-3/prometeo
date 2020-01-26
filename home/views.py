from django.shortcuts import render, redirect
from .models import *
from events.models import *
from datetime import datetime

# Create your views here.
def home(request):
    carousel = Carousel.objects.all()
    min_dt = datetime(2020, 1, 28, 12, 0)
    now = datetime.now()
    next_events = []
    for event in Event.objects.all():
        if (event.date and event.time):
            next_dt = datetime.combine(event.date, event.time)
            if(next_dt <= min_dt and next_dt >= now):
                if (next_dt == min_dt):
                    next_events.append(event)
                else:
                    next_events = [event]
                min_dt = next_dt
    next_dt_str = min_dt.strftime('%Y/%m/%d %H:%M:%S')
    
    return render(request, 'home.html', {'carousel' : carousel, 'next_events': next_events, 'next_dt':min_dt, 'next_dt_str' : next_dt_str, 'next_count' : len(next_events)})

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
