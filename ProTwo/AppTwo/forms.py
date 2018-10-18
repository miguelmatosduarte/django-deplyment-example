from django import forms
from AppTwo.models import User

class Sign_Up_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
