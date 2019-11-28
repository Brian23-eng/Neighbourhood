from django.shortcuts import render,redirect
from . models import *

def home(request):
    title = 'NeighbourHood'
    return render(request, 'landing/index.html', {'title': title})

def hoods(request):
    all_hoods = Neigbourhood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods
    }
    
    return render(request, 'all_hoods.html', params)