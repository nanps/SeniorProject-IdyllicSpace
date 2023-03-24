from django.contrib import admin
from . models import SpaceRoom, UserManage, ChatMessage

# Register your models here.
admin.site.register(SpaceRoom)
admin.site.register(UserManage)
admin.site.register(ChatMessage)