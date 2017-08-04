from django.shortcuts import render, get_object_or_404, redirect
from .models import Activity
from .forms import ActivityForm

def homepage(request):
    return render(request, 'wedding/homepage.html', {})

def rsvp(request):
    return render(request, 'wedding/rsvp.html', {})

def guestbook(request):
    return render(request, 'wedding/guestbook.html', {})

def contact(request):
    return render(request, 'wedding/contact.html', {})

def activity_list(request):
    activities = Activity.objects.order_by('deadline')
    return render(request, 'wedding/activity_list.html', {'activities':activities})

def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'wedding/activity_detail.html', {'activity': activity})

def activity_new(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.save()
            return redirect('activity_detail', pk=activity.pk)
    else:
        form = ActivityForm()
    return render(request, 'wedding/activity_edit.html', {'form': form})

def activity_edit(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.save()
            return redirect('activity_detail', pk=activity.pk)
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'wedding/activity_edit.html', {'form': form})

def activity_remove(request, pk):
    activity =get_object_or_404(Activity, pk=pk)
    activity.delete()
    return redirect('activity_list')