from django.db import models
from django.contrib.auth.models import User


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
