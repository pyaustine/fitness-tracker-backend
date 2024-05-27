from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile'
    )
    bio = models.TextField(null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # In meters
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # In kilograms
    age = models.PositiveIntegerField(null=True, blank=True)
    fitness_goals = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"