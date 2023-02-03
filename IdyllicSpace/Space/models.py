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
    mood = models.CharField(max_length=30, null=True, blank=False)

class Message(models.Model):
    room = models.ForeignKey(SpaceRoom, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

