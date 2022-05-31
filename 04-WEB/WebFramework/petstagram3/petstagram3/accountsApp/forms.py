from datetime import date
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from petstagram3.accountsApp.models import AppUser
from petstagram3.mainApp.models import Profile
from petstagram3.utils import ApplyStyleMixin


class CreateProfileForm(ApplyStyleMixin, UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter first name'},
        )
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter last name'},
        )
    )
    avatar = forms.URLField(
        label='Link to Profile Picture',
        widget=forms.URLInput(
            attrs={'placeholder': 'EnterURL'},
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style()

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            avatar=self.cleaned_data['avatar'],
            user=user
        )
        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter username'
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'placeholder': 'Enter password'
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'placeholder': 'Enter password again'
                }
            )
        }


class EditProfileForm(ApplyStyleMixin, forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter first name'},
        )
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter last name'},
        )
    )
    avatar = forms.URLField(
        label='Link to Profile Picture',
        widget=forms.URLInput(
            attrs={'placeholder': 'Enter URL'},
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Enter email'
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter description',
                'rows': 5
            }
        )
    )

    gender = forms.ChoiceField(
        choices=Profile.genders_list
    )
    birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'label': 'Date of Birth',
                'type': 'date',
                'min': '1920-01-01',
                'max': date.today()
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style()
        self.initial['gender'] = Profile.genders_list[2][1]

    class Meta:
        model = get_user_model()
        fields = ('username',)


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        profile = self.instance
        for pet in profile.pet_set.all():
            [x.delete() for x in pet.petphoto_set.all()]
            pet.delete()
        self.instance.delete()

    class Meta:
        model = AppUser
        fields = tuple()
