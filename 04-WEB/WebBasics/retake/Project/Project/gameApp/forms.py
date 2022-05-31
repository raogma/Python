from django import forms

from Project.gameApp.models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()

    def disable_fields(self):
        for field in self.fields:
            self.fields[field].disabled = True

    class Meta:
        model = Game
        fields = '__all__'
        # widget = {
        #     'title': forms.TextInput(
        #         attrs={                       ## todo doesnt want to delete
        #             'unique':False,
        #         },
        #     )
        # }
