from django.shortcuts import render, redirect

from Expenses.utils import get_first_profile, get_all_expenses


def home(req):
    profile = get_first_profile()
    ctx = {
        'profile': profile,
    }
    if profile:
        expenses = get_all_expenses()
        total_price = sum([x.price for x in expenses])
        ctx['exps'] = expenses
        ctx['total_price'] = total_price
        ctx['money_left'] = profile.budget - total_price
        return render(req, 'home-with-profile.html', ctx)
    return redirect('profileCreate')
