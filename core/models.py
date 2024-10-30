from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('it_staff', 'IT Staff'),
        ('ceso_staff', 'CESO Staff'),
        ('employee', 'Employee'),
        ('student', 'Student'), 
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username