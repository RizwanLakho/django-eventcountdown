# views.py
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import EventForm
from .models import Event


def countdown_timer(request):
    # Get all future events
    current_time = timezone.now()
    events = Event.objects.filter(end_time__gt=current_time).order_by("end_time")

    events_data = []
    for event in events:
        time_remaining = event.end_time - current_time
        total_seconds = int(time_remaining.total_seconds())
        if total_seconds > 0:
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            events_data.append(
                {
                    "id": event.id,
                    "name": event.title,
                    "description": event.description,
                    "hours": hours,
                    "minutes": minutes,
                    "seconds": seconds,
                }
            )

    return render(request, "countdown_timer.html", {"events": events_data})


def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("countdown_timer")
    else:
        form = EventForm()
    return render(request, "add_event.html", {"form": form})
