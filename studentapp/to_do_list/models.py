from django.db import models

class Task(models.Model):
    CATEGORY_CHOICES = [
        ("academic", "Academic"),
        ("personal", "Personal"),
        ("deadline", "Deadline"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
