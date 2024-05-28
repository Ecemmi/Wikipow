from django.db import models
from django.contrib.auth.models import User

class Trail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    length = models.FloatField()  # Trail length in kilometers
    data = models.JSONField()  # Store GPS data as JSON

    def __str__(self):
        return self.name
