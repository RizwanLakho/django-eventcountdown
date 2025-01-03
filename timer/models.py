# models.py
from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event_date = models.DateField()
    event_time = models.TimeField(default="00:00")
    end_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Combine date and time into end_time
        self.end_time = timezone.make_aware(
            timezone.datetime.combine(self.event_date, self.event_time)
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
