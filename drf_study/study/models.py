from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Study(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=180)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
