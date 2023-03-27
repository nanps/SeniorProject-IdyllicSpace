from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SpaceRoom(models.Model) :
    roomName = models.CharField(max_length=20, blank=False, null=False)
    slug = models.SlugField(unique=True, null=True)
    capacity = models.IntegerField(null=True)
    description = models.CharField(max_length=160, null=True, blank=True)
    location = models.CharField(max_length=50, null=True)

    def __str__(self) :
        return self.roomName

class UserManage(models.Model) :
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, null=False)
    displayName = models.CharField(max_length=20, blank=False, null=True)
    avatar =  models.CharField(max_length=30, null=True, blank=False)
    bio = models.CharField(max_length=50, null=True, blank=True)
    mood = models.CharField(max_length=6, null=True, blank=False)
    currentSpaceRoom = models.CharField(max_length=400, null=True)

    def __str__(self) :
        return self.displayName

class ChatMessage(models.Model) :
    slug = models.CharField(max_length=50, blank=False, null=False)
    displayName = models.ForeignKey(UserManage, on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=False, primary_key=True)

    def __str__(self) :
        return self.content
    
# class SpaceRoomManage(models.Model) :
#     slug = models.CharField(max_length=30, blank=False, null=False)
#     capacity = models.ForeignKey(SpaceRoom, on_delete=models.CASCADE, null=True)
#     inRoom = models.IntegerField(null=True)


