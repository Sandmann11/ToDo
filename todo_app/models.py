from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):        
        return self.name

    def get_absolute_url(self):
        return reverse('category_list')


class Task(models.Model):
    PRIORITY = (
        ('Lowest', 'Lowest'),
        ('Low', 'Low'),
        ('Normal', 'Normal'),
        ('High', 'High'),
        ('Highest', 'Highest'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=100, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    priority = models.CharField(max_length=255, null=True, choices=PRIORITY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_due = models.DateField(null=True, blank=True)
    # reminder = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('task_details', kwargs={'pk': self.pk})
        return reverse('task_list')

