from django.shortcuts import render
from .models import HelloWorld

# Create your views here.
def home(request):
    worlds = HelloWorld.objects
    return render(request,'jobs/home.html', {'worlds': worlds})
