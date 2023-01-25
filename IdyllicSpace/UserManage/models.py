from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserManage(models.Model) :
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, null=False)
    displayName = models.CharField(max_length=20, blank=False, null=True)
    avatar =  models.CharField(max_length=30, null=True, blank=False)
    bio = models.CharField(max_length=50, null=True, blank=True)
    mood = models.CharField(max_length=30, null=True, blank=False)
