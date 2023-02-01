from django import forms
from django.forms import ModelForm
from .models import UserManage, SpaceRoom

class DisplayNameForm(ModelForm) :
    class Meta:
        model = UserManage
        fields = ('displayName',)

class AvatarForm(ModelForm) :
    class Meta:
        model = UserManage
        fields = ('avatar',)

class SpaceRoomForm(ModelForm) :
    class Meta:
        model = SpaceRoom
        fields = '__all__'