from django import forms
from django.forms import ModelForm
from .models import UserManage

class DisplayNameForm(ModelForm) :
    class Meta:
        model = UserManage
        fields = ('displayName',)

class AvatarForm(ModelForm) :
    class Meta:
        model = UserManage
        fields = ('avatar',)