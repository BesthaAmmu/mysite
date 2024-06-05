from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.email

class Task(models.Model):
    # name = models.CharField(max_length=255)
    # date_time = models.DateTimeField()
    # assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_assigned')
    # assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created')
    # status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.name
