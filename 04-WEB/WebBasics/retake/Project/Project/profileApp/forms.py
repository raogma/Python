from django import forms

from Project.gameApp.models import Game
from Project.profileApp.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }


class EidtProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # widgets = {
        #     'password': forms.PasswordInput()
        # }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()
        # widgets = {
        #     'password': forms.PasswordInput()
        # }