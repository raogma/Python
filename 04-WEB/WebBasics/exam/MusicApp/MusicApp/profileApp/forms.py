from django import forms

from MusicApp.mainApp.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age'
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, *args):
        self.instance.delete()
        [x.delete() for x in Album.objects.all()]
        return self.instance

    class Meta:
        model = Profile
        fields = ()
