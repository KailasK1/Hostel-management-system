from django import forms
from .models import Room
from .models import User

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'rent', 'is_vacant']  # Include the fields you need

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'start_date', 'end_date']