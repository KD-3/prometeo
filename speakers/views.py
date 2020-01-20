from django.shortcuts import render
from .models import *

# Create your views here.
def speakers(request):
    speakers = Speaker.objects.all()
    return render(request, 'speakers.html', {'speakers':speakers})