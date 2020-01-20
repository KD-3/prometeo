from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from .models import CustomUser, Team
import uuid
import requests
from .forms import *
from events.models import Event
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from allauth.account.signals import user_signed_up
from django.dispatch.dispatcher import receiver


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def user_profile(request):
    types = ['technical', 'informal', 'workshop']
    categories = [] 
    for type in types:
        if(request.user.events.filter(type=type).exists()):
            categories.append(type)
    events = {}
    for event in request.user.events.all():
        if (event.participation_type == 'team'):
            events[event.pk] = request.user.teams.get(event=event).name
    return render(request, 'profile.html', {'categories':categories, 'events' : events})

@login_required
def make_ambassador(request):
    if(request.user.ambassador):
        return redirect('user_profile')
    else:
        request.user.ambassador = True
        request.user.invite_referral = 'CA' + str(uuid.uuid4().int)[:6]
        request.user.save()
        send_mail(
            'Campus Ambassador Invite Referral Code',
            f'You have just registered as Campus Ambassador. Your invite referral code is {request.user.invite_referral}. You can share this code with your friends and invite them to the fest to get exciting benefits.',
            'info.noreply@prometeo.com',
            [request.user.email],
            fail_silently=False,
        )
        messages.success(request, 'You have successfully become a Campus Ambassador. Your invite referral code has been sent to your registered email ID.')

        return redirect('user_profile')

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
                elif team.event in request.user.events.all():
                    form.add_error(None, 'You have already registered for the event ' + team.event.name + ' from a different team')
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
        messages.success(request, f"Successfully joined team '{team.name}'.")
        return redirect('event', team.event.type, team.event.pk)
    else:
        return render(request, 'join_team_confirm.html', {'team':team})

@receiver(user_signed_up) 
def user_signed_up_(request, user, **kwargs):
    if user.ambassador:
        send_mail(
            'Campus Ambassador Invite Referral Code',
            f'You have just registered as Campus Ambassador. Your invite referral code is {user.invite_referral}. You can share this code with your friends and invite them to the fest to get exciting benefits.',
            'info.noreply@prometeo.com',
            [user.email],
            fail_silently=False,
        )
        messages.success(request, 'Your Campus Ambassador invite referral code has been mailed to your registered email ID.')

    
@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            # current_user = form.save(commit=False)
            # if (current_user.ambassador):
            #     current_user.invite_referral = 'CA' + str(uuid.uuid4().int)[:6]
            #     send_mail(
            #         'Campus Ambassador Invite Referral Code',
            #         f'You have just registered as Campus Ambassador. Your invite referral code is {user.invite_referral}. You can share this code with your friends and invite them to the fest to get exciting benefits.',
            #         'info.noreply@prometeo.com',
            #         [request.user.email],
            #         fail_silently=False,
            #     )
            #     messages.success(request, 'Your Campus Ambassador invite referral code has been mailed to your registered email ID.')
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('user_profile')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})