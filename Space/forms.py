from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
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

class MoodForm(ModelForm) :
    class Meta:
        model = UserManage
        fields = ('mood',)

class CurrentSpaceRoomForm(ModelForm) :
    class Meta:
        model = UserManage
        fields = ('currentSpaceRoom',)

class LeaveRoomForm(ModelForm) :
    class Meta:
        model = SpaceRoom
        fields = ('inRoom', 'roomStatus',)

class PasswordChangingForm(PasswordChangeForm) :
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']