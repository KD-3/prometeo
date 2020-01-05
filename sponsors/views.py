from django.shortcuts import render, redirect
from .models import Sponsor
# from users.models import CustomUser
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def sponsors(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'sponsors.html', {'sponsors' : sponsors})