from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=280)
    details = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    # created_date = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    # due_date = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    # requester = 
    # tasker = 

    def __str__(self):
        return self.text



