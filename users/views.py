from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from .models import CustomUser, Team
import uuid
from .forms import CustomUserCreationForm, TeamCreationForm, TeamJoiningForm

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
def create_team(request):
    if request.method == 'POST':
        form = TeamCreationForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.id = 'PRO' + str(uuid.uuid4().int)[:6]
            team.leader = request.user
            team.save()
            team.members.add(request.user)
            team.save()
            # form.save_m2m()
            return redirect('team_created', team=team)
    else:
        form = TeamCreationForm()
    return render(request, 'create_team.html', {'form': form})

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
                else:
                    team.members.add(request.user)
                    team.save()
                    return redirect('home')
            else:
                form.add_error('teamId', 'No team with the given team ID exists')
            # form.save_m2m()
            
    else:
        form = TeamJoiningForm()
    return render(request, 'join_team.html', {'form': form})

def team_created(request):
    return render(request, 'team_created.html')