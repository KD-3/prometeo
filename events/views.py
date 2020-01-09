import os
from django.shortcuts import render, redirect
# import os
from django.conf import settings
from .models import Event
from users.models import CustomUser
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
import xlsxwriter


# Create your views here.
def events(request, type):
    # print(type)
    events = Event.objects.all()
    teams = {}
    if(request.user.is_authenticated):
        for event in events:
            if(event.participation_type == 'team' and request.user.teams.filter(event=event).exists()):
                teams[event.pk] = request.user.teams.get(event=event)
    return render(request, 'events.html', {'events' : events, 'type' : type, 'teams':teams})

def event(request, type, eventid):
    event = get_object_or_404(Event, pk=eventid)
    if (request.user.is_superuser):
        participants = event.participants.all()
        wbname = event.name + ' (' + event.type + ') Participants.xlsx'
        wbpath = os.path.join(settings.MEDIA_ROOT, os.path.join('workbooks', wbname))
        workbook = xlsxwriter.Workbook(wbpath)
        worksheet = workbook.add_worksheet(event.name)
        col_center = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
        })
        worksheet.set_column(0, 1, 70, col_center)
        merge_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
        })
        header_format = workbook.add_format({
            'bold' : 1,
            'align': 'center',
            'valign': 'vcenter',
        })
        worksheet.merge_range('A1:B1', event.name + ' Participants', merge_format)
        worksheet.write(1, 0, "Username", header_format)
        worksheet.write(1, 1, "Email", header_format)
        row = 2
        for participant in participants:
            worksheet.write(row, 0, participant.username)
            worksheet.write(row, 1, participant.email)
            row = row + 1
        workbook.close()
        return render(request, 'event.html', {'participants' : participants, 'event' : event, 'wbname' : wbname})
    if(request.user.is_authenticated):
        if(event.participation_type == 'team'):
            if(request.user.teams.filter(event=event).exists()):
                team = request.user.teams.get(event=event)
                return render(request, 'event.html', {'event':event, 'team':team})
    return render(request, 'event.html', {'event' : event})
    

def speakers(request):
    events = Event.objects.all()
    return render(request, 'speakers.html', {'events' : events})

@login_required
def registered(request):
    events = request.user.events.all()
    types = ['technical', 'informal', 'workshop']
    categories = [] 
    for type in types:
        if(request.user.events.filter(type=type).exists()):
            categories.append(type)
    return render(request, 'registered.html', {'events' : events, 'categories':categories})

@login_required
def register_for_event(request, eventid):
    request.user.events.add(Event.objects.get(pk=eventid))
    return redirect(registered)
