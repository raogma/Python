import os

from django import forms

from Expenses.mainApp.models import Profile
from Expenses.utils import get_all_expenses


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        widgets = {
            'profile_image': forms.FileInput(
                attrs={
                    'class': 'form-file'
                }
            ),
        }


class ProfileFormDelete(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, *args):
        expenses = get_all_expenses()
        [x.delete() for x in expenses]
        file_path = self.instance.profile_image.path
        self.instance.delete()
        os.remove(file_path)
        return self.instance

    class Meta:
        model = Profile
        fields = tuple()
