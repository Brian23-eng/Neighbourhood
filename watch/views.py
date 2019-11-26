from django.shortcuts import render,redirect

def home(request):
    title = 'NeighbourHood'
    return render(request, 'home.html', {'title': title})
