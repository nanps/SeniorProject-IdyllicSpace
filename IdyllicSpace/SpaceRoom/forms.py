from django.forms import ModelForm
from .models import SpaceRoom

class SpaceRoomForm(ModelForm) :
    class Meta:
        model = SpaceRoom
        fields = '__all__'