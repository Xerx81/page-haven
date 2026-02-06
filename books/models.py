from django.db import models
from uuid import uuid4


class Book(models.Model):
    STATUS_CHOICES = [
        ("read", "Read"), 
        ("reading", "Reading"),
        ("plan_to_read", "Plan to Read"), 
        ("on_hold", "On Hold"), 
        ("dropped", "Dropped"),
    ]

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    bookmark = models.PositiveIntegerField(blank=True, default=0)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
