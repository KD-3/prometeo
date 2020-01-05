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
def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events' : events})

def event(request, eventid):
    event = get_object_or_404(Event, pk=eventid)
    # print(event.name)
    is_registered = False
    user_events = request.user.events.all()
    for _event in user_events:
        # print(_event.name)
        if _event.pk == event.pk:
            # print ('True')
            is_registered = True
            break
    return render(request, 'event.html', {'event' : event, 'is_registered' : is_registered})

def speakers(request):
    events = Event.objects.all()
    return render(request, 'speakers.html', {'events' : events})

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
    return redirect(events)

@user_passes_test(lambda u: u.is_superuser)
def registered_users(request, eventid):
    event = get_object_or_404(Event, pk=eventid)
    participants = event.participants.all()
    workbook = xlsxwriter.Workbook(os.path.join(settings.MEDIA_ROOT, os.path.join('workbooks', event.name + ' Participants.xlsx')))
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
    return render(request, 'event.html', {'participants' : participants, 'event' : event})
    return redirect(registered)
