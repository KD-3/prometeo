from django.shortcuts import render, redirect
from .models import Event
from users.models import CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events' : events})

def event(request, eventid):
    event = get_object_or_404(Event, pk=eventid)
    return render(request, 'event.html', {'event' : event})

@login_required
def register_for_event(request, eventid):
    request.user.events.add(Event.objects.get(pk=eventid))
    return redirect(events)
