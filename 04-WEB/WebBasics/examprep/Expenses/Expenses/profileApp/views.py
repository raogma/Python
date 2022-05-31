from django.shortcuts import render

from Expenses.mainApp.models import Expense
from Expenses.profileApp.forms import ProfileForm, ProfileFormDelete
from Expenses.utils import crud, get_first_profile, get_all_expenses

profile = get_first_profile()


def profile_details(req):

    ctx = {
        'profile': profile,
    }
    if profile:
        expenses = get_all_expenses()
        total_expenses_count = len(expenses)
        money_left = profile.budget - sum([x.price for x in expenses])
        ctx['total_expenses_count'] = total_expenses_count
        ctx['money_left'] = f'{money_left:.2f}'
    return render(req, 'profile.html', ctx)


def create_profile(req):
    return crud(req, ProfileForm, None, 'homePath', 'home-no-profile.html')


def edit_profile(req):
    return crud(req, ProfileForm, profile, 'profileDetails', 'profile-edit.html')


def delete_profile(req):
    return crud(req, ProfileFormDelete, profile, 'homePath', 'profile-delete.html')
