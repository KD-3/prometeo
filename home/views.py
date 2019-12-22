from django.shortcuts import render, redirect
from .models import Carousel

# Create your views here.
def home(request):
    carousel = Carousel.objects.all()
    return render(request, 'home.html', {'carousel' : carousel})

def home_redirect(request):
    return redirect(home)