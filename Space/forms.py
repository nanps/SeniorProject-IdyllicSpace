from django import forms
from django.forms import ModelForm
from .models import UserManage, SpaceRoom, ChatMessage

class DisplayNameForm(ModelForm) :
    class Meta:
        model = UserManage
        fields = ('displayName',)

class AvatarForm(ModelForm) :
    class Meta:
        model = UserManage
        fields = ('avatar',)

class MessageForm(ModelForm) :
    class Meta:
        model = ChatMessage
        fields = ('slug','content',)

class SpaceRoomForm(ModelForm) :
    class Meta:
        model = SpaceRoom
        fields = '__all__'

class BioForm(ModelForm) :
    class Meta:
        model = UserManage
        fields = ('bio',)

class CurrentSpaceRoomForm(ModelForm) :
    class Meta:
        model = UserManage
        fields = ('currentSpaceRoom',)
