from django.db import models
from django.utils import timezone

class Activity(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    assigned_to = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
