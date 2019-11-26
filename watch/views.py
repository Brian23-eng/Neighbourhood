from django.shortcuts import render,redirect

def home(request):
    title = 'NeighbourHood'
    return render(request, 'landing/home.html', {'title': title})
