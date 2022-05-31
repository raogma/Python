from django import forms

from Expenses.mainApp.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseFormDelete(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()

    def disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, *args, **kwargs):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = '__all__'
