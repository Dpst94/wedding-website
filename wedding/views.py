from django.shortcuts import render

def homepage(request):
    return render(request, 'wedding/homepage.html', {})

def activities(request):
    pass