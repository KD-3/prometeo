from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .models import CustomUser

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@user_passes_test(lambda u: u.is_superuser)
def users_info(request):
    users = CustomUser.objects
    return render(request, 'users_info.html', {'users':users})

@user_passes_test(lambda u: u.is_superuser)
def events_info(request, userid):
    user = CustomUser.objects.get(pk=userid)
    return render(request, 'events_info.html', {'query_user':user})