from datetime import date

from django import forms

from petstagram3.mainApp.models import Pet
from petstagram3.utils import ApplyStyleMixin, get_years_choice, DisableFieldsMixin


class CreatePetForm(ApplyStyleMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style()
        # self.initial['user']

    types_list = [
        ("Cat", "Cat"),
        ("Dog", "Dog"),
        ("Bunny", "Bunny"),
        ("Parrot", "Parrot"),
        ("Fish", "Fish"),
        ("Other", "Other")
    ]

    class Meta:
        model = Pet
        fields = ('name', 'type', 'birth')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter pet name'
            }),
            'birth': forms.DateInput(attrs={
                'label': 'Day of Birth',
                'type': 'date',
                'min': '1920-01-01',
                'max': date.today()
            })
        }


class EditPetForm(ApplyStyleMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style()

    class Meta:
        model = Pet
        exclude = ('owner', )
        widgets = {
            'birth': forms.SelectDateWidget(
                years=get_years_choice()
            )
        }


class DeletePetForm(ApplyStyleMixin, DisableFieldsMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style()
        self.disable() #TODO

    def save(self, *args, **kwargs):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        exclude = ('owner', )
