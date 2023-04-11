from django.contrib import admin
from . models import SpaceRoom, UserManage, ChatMessage, RoomMember

# Register your models here.
admin.site.register(SpaceRoom)
admin.site.register(UserManage)
admin.site.register(ChatMessage)
admin.site.register(RoomMember)