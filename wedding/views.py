from django.shortcuts import render, get_object_or_404
from .models import Activity

def homepage(request):
    return render(request, 'wedding/homepage.html', {})

def activities(request):
    activities = Activity.objects.order_by('deadline')
    return render(request, 'wedding/activities.html', {'activities':activities})

def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'wedding/activity_detail.html', {'activity': activity})