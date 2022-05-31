from django import forms

from MusicApp.mainApp.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'image_URL': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price'
                }
            ),
        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()

    def save(self, *args):
        self.instance.delete()
        return self.instance

    def disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            # field.widget.attrs['readonly'] = 'readonly'
            field.required = False

    class Meta:
        model = Album
        fields = '__all__'
