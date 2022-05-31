from datetime import date

from django.shortcuts import render, redirect
from django.urls import reverse_lazy


class SuccessRedirectMixin:
    def redirect_to_dash(self):
        return reverse_lazy('dashPath')


class DisableFieldsMixin:
    def disable(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'


class ApplyStyleMixin:
    def apply_style(self):
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


def sendRequest(req, form_cls, instance_cls, template, redirect_to, pk=None):
    if req.method == 'POST':
        form = form_cls(req.POST, req.FILES, instance=instance_cls)
        if form.is_valid():
            form.save()
            return redirect(redirect_to)

    form = form_cls(instance=instance_cls)

    ctx = {
        'form': form
    }
    if pk:
        ctx['pk'] = pk
    return render(req, template, ctx)


def get_years_choice():
    today = str(date.today())
    today = int(today.split('-')[0])
    return [str(x) for x in range(1920, today + 1)]
