from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from .models import CustomUser, Team
import uuid
import requests
from .forms import CustomUserCreationForm, TeamCreationForm, TeamJoiningForm
from events.models import Event
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@user_passes_test(lambda u: u.is_superuser)
def users_info(request):
    users = CustomUser.objects
    return render(request, 'users_info.html', {'users':users})

@user_passes_test(lambda u: u.is_superuser)
def user_info(request, userid):
    user = CustomUser.objects.get(pk=userid)
    return render(request, 'user_info.html', {'query_user':user})

@login_required
def create_team(request, eventid):
    event = get_object_or_404(Event, pk=eventid)
    if(request.user.teams.filter(event=event).exists()):
        return redirect('event', event.type, event.pk)
    if request.method == 'POST':
        form = TeamCreationForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.id = 'PRO' + str(uuid.uuid4().int)[:6]
            team.leader = request.user
            team.event = event
            team.save()
            team.members.add(request.user)
            team.save()
            request.user.events.add(event)
            message = f'You have just created team "{team.name}" for the {event.type} event {event.name}. The team ID is {team.id}. Share this ID with your friends who can join your team using this ID.'
            send_mail(
                'Team Details',
                message,
                'info.noreply@prometeo.com',
                [request.user.email],
                fail_silently=False,
            )
            # form.save_m2m()
            return redirect('team_created')
    else:
        form = TeamCreationForm()
    return render(request, 'create_team.html', {'form': form, 'event':event})

@login_required
def join_team(request):
    if request.method == 'POST':
        form = TeamJoiningForm(request.POST)
        if form.is_valid():
            teamId = form.cleaned_data['teamId']
            if(Team.objects.filter(pk=teamId).exists()):
                team = Team.objects.get(pk=teamId)
                if request.user in team.members.all():
                    form.add_error(None, 'You are already a member of this team')
                elif (team.members.all().count() >= team.event.max_team_size):
                    form.add_error(None, 'Team is already full')
                else:
                    response = redirect('join_team_confirm')
                    response['Location'] += '?id=' + teamId
                    return response
                    
            else:
                form.add_error('teamId', 'No team with the given team ID exists')
            # form.save_m2m()
            
    else:
        form = TeamJoiningForm()
    return render(request, 'join_team.html', {'form': form})

def team_created(request):
    return render(request, 'team_created.html')

def join_team_confirm(request):
    teamId = request.GET['id']
    team = Team.objects.get(pk=teamId)
    if request.method == 'POST':
        team.members.add(request.user)
        team.save()
        request.user.events.add(team.event)
        messages.success(request, 'Successfully joined team.')
        return redirect('event', team.event.type, team.event.pk)
    else:
        return render(request, 'join_team_confirm.html', {'team':team})