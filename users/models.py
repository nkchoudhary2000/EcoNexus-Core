from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom User model for EcoNexus.
    """
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username
