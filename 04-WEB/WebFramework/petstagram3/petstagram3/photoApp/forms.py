from django import forms

from petstagram3.mainApp.models import PetPhoto
from petstagram3.utils import ApplyStyleMixin


class CreatePhotoForm(ApplyStyleMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style()

    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')
        widgets = {
            'photo': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Enter description'
                }
            ),
        }


class EditPhotoForm(ApplyStyleMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style()

    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets',)
