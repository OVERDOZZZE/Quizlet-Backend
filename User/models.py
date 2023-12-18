from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='images/user_avatars/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

