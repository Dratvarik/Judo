from attr import field
from django import forms
from .models import Userss

class UserssForm(forms.ModelForm):
    class Meta:
        model = Userss()
        fields = "__all__"