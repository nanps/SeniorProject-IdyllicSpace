from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SpaceRoom(models.Model) :
    roomName = models.CharField(max_length=20, blank=False, null=False)
    slug = models.SlugField(unique=True, null=False, primary_key=True)
    capacity = models.IntegerField(null=False)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=10, null=False)
    inRoom = models.IntegerField(null=True)
    roomStatus = models.CharField(max_length=5, null=False)  #open, close, full

    def __str__(self) :
        return self.roomName

class UserManage(models.Model) :
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, null=False)
    displayName = models.CharField(max_length=20, blank=False, null=True)
    avatar =  models.CharField(max_length=12, null=True, blank=False)
    bio = models.TextField(null=True, blank=True)
    mood = models.CharField(max_length=6, null=True, blank=False)
    currentSpaceRoom = models.CharField(max_length=45, null=True)

    def __str__(self) :
        return self.displayName
    
class ChatMessage(models.Model) :
    slug = models.CharField(max_length=40, blank=False, null=False)
    displayName = models.ForeignKey(UserManage, on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=False, primary_key=True)

    # slug = models.CharField(max_length=40, blank=False, null=False)
    # displayName = models.ForeignKey(UserManage, on_delete=models.CASCADE, null=False)
    # content = models.TextField(blank=False, null=False)

    def __str__(self) :
        return self.content