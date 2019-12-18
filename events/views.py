from django.shortcuts import render
from .models import Event
from users.models import CustomUser
from django.shortcuts import get_object_or_404

# Create your views here.
def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events' : events})

def event(request, eventid):
    event = get_object_or_404(Event, pk=eventid)
    return render(request, 'event.html', {'event' : event})

def register_for_event(request, eventid):
    if request.user.is_authenticated:
        request.user.events.add(Event.objects.get(pk=eventid))
    else:
        pass
    return render(request, 'events.html')
