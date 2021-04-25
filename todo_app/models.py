from django.db import models
from django.urls import reverse


class Task(models.Model):
    PRIORITY = (
        ('Lowest', 'Lowest'),
        ('Low', 'Low'),
        ('Normal', 'Normal'),
        ('High', 'High'),
        ('Highest', 'Highest'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True, blank=True)
    details = models.TextField()
    category = models.CharField(max_length=255)
    priority = models.CharField(max_length=200, null=True, choices=PRIORITY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_due = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('task_details', kwargs={'pk': self.pk})
        return reverse('task_list')