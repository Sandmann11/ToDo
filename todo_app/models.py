from django.db import models


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

    def __str__(self):
        return self.name