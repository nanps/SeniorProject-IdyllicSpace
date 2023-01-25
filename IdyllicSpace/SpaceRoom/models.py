from django.db import models

# Create your models here.
class SpaceRoom(models.Model) :
    roomName = models.CharField(max_length=20, blank=False, null=False)
    capacity = models.IntegerField(null=True)
    description = models.CharField(max_length=160, null=True, blank=True)
    location = models.CharField(max_length=50, null=True)

    def __str__(self) :
        return self.roomName
