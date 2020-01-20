from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from users.models import *
# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def users_info(request):
    users = CustomUser.objects.all()
    return render(request, 'dashboard/users_info.html', {'users':users})

@user_passes_test(lambda u: u.is_superuser)
def user_info(request, username):
    user = get_object_or_404(CustomUser, username=username)
    teams = {}
    for team in user.teams.all():
        teams[team.event.pk] = team.name
    return render(request, 'dashboard/user_info.html', {'cur_user':user, 'teams' : teams})