from django import forms
from .models import Userss

class UsersForm(forms.ModelForm):
    class Meta:
        model = Userss
        fields = "__all__"