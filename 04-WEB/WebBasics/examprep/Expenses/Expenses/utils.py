from django.shortcuts import redirect, render

from Expenses.mainApp.models import Profile, Expense


def get_first_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]


def get_all_expenses():
    return Expense.objects.all()


def crud(req, form_cls, instance_cls, redirect_target, template):
    if req.method == 'POST':
        form = form_cls(req.POST, req.FILES, instance=instance_cls)
        if form.is_valid():
            form.save()
            return redirect(redirect_target)
    else:
        form = form_cls(instance=instance_cls)
    ctx = {
        'form': form
    }
    return render(req, template, ctx)
