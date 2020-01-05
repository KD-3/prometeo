from django.shortcuts import render, redirect
from .models import Event
from users.models import CustomUser
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events' : events})

def event(request, eventid):
    event = get_object_or_404(Event, pk=eventid)
    return render(request, 'event.html', {'event' : event})

@login_required
def registered(request):
    events = request.user.events.all()
    return render(request, 'registered.html', {'events' : events})

def workshops(request):
    events = Event.objects.all()
    return render(request, 'workshops.html', {'events' : events})

def informals(request):
    events = Event.objects.all()
    return render(request, 'informals.html', {'events' : events})

@login_required
def register_for_event(request, eventid):
    request.user.events.add(Event.objects.get(pk=eventid))
    return redirect(registered)
