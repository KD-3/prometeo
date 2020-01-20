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
from django.contrib import messages

# Create your views here.
def events(request, type):
    events = Event.objects.filter(type=type)
    if(request.user.is_superuser):
        wbname = f'Events ({type}) Participation List.xlsx'
        wbpath = os.path.join(settings.MEDIA_ROOT, os.path.join('workbooks', wbname))
        workbook = xlsxwriter.Workbook(wbpath)
        for event in events:
            worksheet = workbook.add_worksheet(event.name)
            col_center = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
            })
            worksheet.set_column(0, 100, 30, col_center)
            worksheet.set_row(0, 30)
            merge_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter',
                'bg_color' : 'gray',
                'font_size' : 20
            })
            header_format = workbook.add_format({
                'bold' : 1,
                'align': 'center',
                'valign': 'vcenter',
                'font_color' : 'white',
                'bg_color' : 'black'
            }) 
            invalid_format = workbook.add_format({
                'bg_color': '#ff7f7f',
                'align': 'center',
                'valign': 'vcenter',
            })
            light_format = workbook.add_format({
                'bg_color': '#d3d3d3',
                'align': 'center',
                'valign': 'vcenter',
            })
            if (event.participation_type == 'individual'):
                worksheet.merge_range('A1:B1', event.name + ' - Participants', merge_format)
                worksheet.write(1, 0, "Username", header_format)
                worksheet.write(1, 1, "Email", header_format)
                row = 2
                for participant in event.participants.all():
                    worksheet.write(row, 0, participant.username)
                    worksheet.write(row, 1, participant.email)
                    if(row%2):
                        worksheet.set_row(row, cell_format=light_format)
                    row = row + 1
            else:
                worksheet.merge_range('A1:H1', event.name + ' - Participanting Teams', merge_format)
                worksheet.write(1, 0, "Team ID", header_format)
                worksheet.write(1, 1, "Team Name", header_format)
                for i in range(1, event.max_team_size+1):
                    worksheet.write(1, i+1, "Member " + str(i), header_format)
                worksheet.write(1, event.max_team_size+2, "Status", header_format)
                row = 2
                for team in event.participating_teams.all():
                    if(row%2):
                        worksheet.set_row(row, cell_format=light_format)
                    worksheet.write(row, 0, team.pk)
                    worksheet.write(row, 1, team.name)
                    i = 2
                    for member in team.members.all():
                        worksheet.write(row, i, member.username + f' ({member.email})')
                        i = i + 1
                    if (team.members.all().count() < event.min_team_size or team.members.all().count() > event.max_team_size):
                        worksheet.write(row, event.max_team_size+2, "INELIGIBLE")
                        worksheet.set_row(row, cell_format=invalid_format)
                    else:
                        worksheet.write(row, event.max_team_size+2, "ELIGIBLE")
                    row = row + 1
        workbook.close()
        return render(request, 'events.html', {'events' : events, 'type' : type, 'wbname' : wbname})
    else:
        return render(request, 'events.html', {'events' : events, 'type' : type})

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
    event = Event.objects.get(pk=eventid)
    request.user.events.add(event)
    messages.success(request, f"Successfully registered for '{event.name}'.")
    return redirect(registered)
